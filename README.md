### This is a tool for pBFT consensus visualization, you can find the pBFT project here [pBFT](https://github.com/bianyuanop/pBFT)

### Color Scheme

| Action      | Color(Hex) | Color                            |
| ----------- | ---------- | -------------------------------- |
| PrePrepare  | #000075    | ![navy](./examples/navy.png)     |
| Prepare     | #42d4f4    | ![navy](./examples/cyan.png)     |
| Commit      | #dcbeff    | ![navy](./examples/lavender.png) |
| NewRound    | #e6194b    | ![navy](./examples/red.png)      |
| RoundChange | #800000    | ![navy](./examples/maroon.png)   |

| State          | Color(Hex) | Color                            |
| -------------- | ---------- | -------------------------------- |
| Prepared       | #42d4f4    | ![navy](./examples/cyan.png)     |
| Committed      | #dcbeff    | ![navy](./examples/lavender.png) |
| NewRound       | #808000    | ![navy](./examples/olive.png)    |
| RoundChange    | #800000    | ![navy](./examples/maroon.png)   |
| FinalCommitted | #911eb4    | ![navy](./examples/purple.png)   |

### Mechanism

In the pBFT, for every node, on receiving messages, they will process messages then write the **action, origin id, target id, round number, phase, time stamp(ms)** into database. This tool will use the messages recorded in database to visualize the processing process of the whole system. **HOWEVER**, due to the record operations happen at the receivers' sides, so we can't know the senders' states at receivers' sides. Except that, the visualization tool works fine.

### Usage

Install dependencies

```
pip install -r requirements.txt
```

Create table in MySQL

![image-20230416145104481](./examples/table.png)

Configure database credentials in `db.py`

Run 

```
python main.py <count:number> # count here means how many messages you want to visualize
```

Before running the script every experiment, you have to clear the data table first.

### Examples

#### f=1

![[video-to-gif output image]](./examples/example.gif)

#### f=2

![example2](./examples/example2.gif)