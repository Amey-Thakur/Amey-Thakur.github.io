import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
from matplotlib.gridspec import GridSpec

# Set FFmpeg path
plt.rcParams['animation.ffmpeg_path'] = r"C:\Users\AMEY THAKUR\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0.1-full_build\bin\ffmpeg.exe"

# Dataset
X1 = np.array([1.0, 3.0, 2.3, 6.0, 1.5, 7.0, 5.0, 3.3, 4.0, 2.0, 3.0, 0.0, 5.5, 4.3])
X2 = np.array([7, 6, 5, 8, 6, 9, 7, 6, 8, 5, 6, 4, 8, 7])  # Example second feature
Y = np.array([35, 55, 42, 94, 36, 96, 90, 70, 80, 39, 50, 34, 95, 83])

# Normalize features for smooth convergence
X1_norm = (X1 - X1.mean()) / X1.std()
X2_norm = (X2 - X2.mean()) / X2.std()
X = np.column_stack((X1_norm, X2_norm))
Y_norm = (Y - Y.mean()) / Y.std()

# Initialize weights and bias
w1, w2, b = np.random.randn(), np.random.randn(), np.random.randn()
lr = 0.05
iterations = 50

# Prepare grid for plane
x1_surf, x2_surf = np.meshgrid(np.linspace(X1_norm.min(), X1_norm.max(), 20),
                               np.linspace(X2_norm.min(), X2_norm.max(), 20))

# Record planes and MSE for each iteration
planes = []
mses = []

# Gradient Descent Simulation
for i in range(iterations):
    Y_pred = w1*X[:,0] + w2*X[:,1] + b
    error = Y_pred - Y_norm
    mse = np.mean(error**2)
    mses.append(mse)
    
    # Compute gradients
    dw1 = (2/len(Y)) * np.dot(error, X[:,0])
    dw2 = (2/len(Y)) * np.dot(error, X[:,1])
    db = (2/len(Y)) * np.sum(error)
    
    # Update weights
    w1 -= lr * dw1
    w2 -= lr * dw2
    b -= lr * db
    
    # Compute plane for current iteration
    Y_plane = w1*x1_surf + w2*x2_surf + b
    planes.append(Y_plane.copy())

# Create figure with GridSpec for plane + MSE plot
fig = plt.figure(figsize=(10,5))
gs = GridSpec(1, 2, width_ratios=[3,1])
ax3d = fig.add_subplot(gs[0], projection='3d')
ax_mse = fig.add_subplot(gs[1])

def animate(i):
    ax3d.cla()
    ax_mse.cla()
    
    # 3D scatter plot
    ax3d.scatter(X1_norm, X2_norm, Y_norm, color='black', label='Data Points')
    
    # Regression plane with color gradient based on predicted values
    surf = ax3d.plot_surface(x1_surf, x2_surf, planes[i], cmap='viridis', alpha=0.7, edgecolor='none')
    
    ax3d.set_xlabel('Normalized Hours Studied (X1)')
    ax3d.set_ylabel('Normalized Attendance (X2)')
    ax3d.set_zlabel('Normalized Grades Received (Y)')
    ax3d.set_title('3D MLR Regression Plane Convergence')
    ax3d.view_init(30, 45)
    
    # MSE plot
    ax_mse.plot(range(i+1), mses[:i+1], color='red')
    ax_mse.set_xlabel('Iteration')
    ax_mse.set_ylabel('MSE')
    ax_mse.set_title('Mean Squared Error Convergence')
    ax_mse.set_xlim(0, iterations)
    ax_mse.set_ylim(0, max(mses)*1.1)

ani = animation.FuncAnimation(fig, animate, frames=iterations, interval=200)
# Saved to current directory (which will be set to the content folder)
ani.save('MLR_3D_MSE_Convergence.mp4', writer='ffmpeg', dpi=150)
print("Video saved successfully.")
