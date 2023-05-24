gl.setup(NATIVE_WIDTH, NATIVE_HEIGHT)

local font = resource.load_font "font.ttf"

function node.render()
    font:write(1000, 500, "Hello world", 64, 1,1,1,1)
end
