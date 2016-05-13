from PIL import Image, ImageTk

# class which may to load images all over the system
class Loader:
    # all objects here
    images = []
    
    # loading object
    def load(self, path, tk=True, size=None):
        # open the image
        self.img = Image.open("src/" + path)
        
        # configure the image
        if not size is None:
            self.img = self.img.resize(size)        
        if tk:
            self.img = ImageTk.PhotoImage(self.img)
        
        # save the image
        self.images.append(self.img)
        
        return self.images[-1]