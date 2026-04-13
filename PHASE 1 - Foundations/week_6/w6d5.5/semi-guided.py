class PipelineRecord:
    """Base class for all pipeline records."""
    def __init__(self, pipe_id, job_name, run_date, status):
        self.pipe_id = pipe_id
        self.job_name = job_name
        self.run_date = run_date
        self.status = status.strip().lower()
        #TODO: store all four as attributes
        #TODO: clean status with .strip().lower()
        

    def is_success(self):
        return self.status == "success"
        #TODO: return True if status == "success"
        

    def summary(self):
        return f"{self.pipe_id} | {self.job_name} | [{self.status}]"
        #TODO: return "pipe_id | job_name [status]"
        


class TimedRecord(PipelineRecord):
    """A pipeline record with timing information."""
    def __init__(self, pipe_id, job_name, run_date, status, duration_seconds):
        super().__init__(pipe_id, job_name, run_date, status)
        self.duration_seconds = duration_seconds
        #TODO: call super().__init__(...) for the first four
        #TODO: store duration_seconds as self attribute
        

    def duration_display(self):
        minutes = self.duration_seconds // 60
        seconds = self.duration_seconds % 60
        #TODO: return "Xm Ys" using // and % (from W1D7)
        return f"{minutes}m {seconds}s"

    def summary(self):
        return f"{self.pipe_id} | {self.job_name} | [{self.status}] | duration : {self.duration_display()}"
        #TODO: override parent — include duration_display() in output
        


class RowCountRecord(TimedRecord):
    """A timed record that also tracks rows processed."""
    def __init__(self, pipe_id, job_name, run_date, status, duration_seconds, rows):
        super().__init__(pipe_id, job_name, run_date, status, duration_seconds)
        self.rows = rows
        #TODO: call super().__init__(...) for the first five
        #TODO: store rows
        

    def rows_per_second(self):
        if self.duration_seconds == 0:
            raise ZeroDivisionError("duration_seconds cannot be zero")
        return self.rows/ self.duration_seconds
        #TODO: return rows / duration_seconds (guard against zero)
        

    def summary(self):
        return f"{self.pipe_id} | {self.job_name} | [{self.status}] | duration : {self.duration_display()} | rows:{self.rows} | rows per second: {round(self.rows_per_second())} "
        #TODO: override — include rows and rows_per_second
        


# Test with your W1D7 pipeline data
records = [
    RowCountRecord("PIPE-01", "etl_customers", "2026-02-09", "SUCCESS", 127, 8420),
    RowCountRecord("PIPE-02", "etl_orders", "2026-02-09", "SUCCESS", 203, 12450),
    TimedRecord("PIPE-03", "etl_products", "2026-02-09", "WARN", 65),
    PipelineRecord("PIPE-04", "etl_events", "2026-02-09", "FAILED"),
]
count = 0
for r in records:
    
    print(r.summary())
    if r.is_success():
        count += 1
print(count)

#TODO: loop and print summary() for each — polymorphism handles different types
#TODO: count how many are successful using is_success()
