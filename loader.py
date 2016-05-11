from PIL import Image, ImageTk

# class which may to load images all over the system
class Loader:
    images = []
    
    # loading object
    def load(self, path, tk=True, size=None):
        self.img = Image.open("src/" + path)
        
        if not size is None:
            self.img = self.img.resize(size)        
        if tk:
            self.img = ImageTk.PhotoImage(self.img)
        
        self.images.append(self.img)
        
        return self.images[-1]