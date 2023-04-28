import settings
class Sphere:
    def __init__(self, x: float, y: float, x_dir: int, y_dir : int) -> None:
        self.x = x
        self.y = y
        self.speed = 3
        self.x_dir = x_dir
        self.y_dir = y_dir

    def update(self) -> None:
        self.x += self.speed * self.x_dir
        self.y += self.speed * self.y_dir
        self.collision()

    def collision(self) -> None:
        if self.x < 0 or self.x > settings.WIDTH:
            self.x_dir *= -1
        if self.y < 0 or self.y > settings.HEIGHT:
            self.y_dir *= -1