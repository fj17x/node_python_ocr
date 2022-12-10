const express = require("express")
const { spawn } = require("child_process")
var multer = require("multer")
const cors = require("cors")
const app = express()
const upload = multer({ dest: "./uploads" })

app.use(cors())
app.post("/ocr", upload.single("photo"), (req, res) => {
  var t
  const python = spawn("python", ["script.py", req.file.path])
  python.stdout.on("data", (d) => {
    t = d.toString()
  })
  python.on("close", () => {
    res.send(t)
  })
})

app.listen(3000)
