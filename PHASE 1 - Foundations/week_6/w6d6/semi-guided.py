from dataclasses import dataclass

@dataclass
class PipelineRun:
    pipe_id: str
    job_name: str
    duration_seconds: int
    rows_processed: int
    status: str

    @property
    def duration_display(self):
        minutes = self.duration_seconds // 60
        seconds = self.duration_seconds % 60
        return f"{minutes}m {seconds}s"
        
        

    @property
    def rows_per_second(self):
        if self.duration_seconds == 0:
            return 0.0          #first i did a raise valueError
        return self.rows_processed / self.duration_seconds
       
        

    @property
    def is_success(self):
        return self.status.lower() == "success"
        
        

    def __str__(self):
        return f"{self.pipe_id} | {self.job_name} | {self.duration_display} {self.rows_processed:,} rows ({round(self.rows_per_second)} r/s) [{self.status.upper()}]"
        #TODO: return formatted string like:
        # "PIPE-01 | etl_customers | 2m 7s | 8,420 rows (66.3 r/s) [SUCCESS]"
        # Hint: use f-strings with :, for thousands separator
        


# Test with your W1D7 data
runs = [
    PipelineRun("PIPE-01", "etl_customers", 127, 8420, "SUCCESS"),
    PipelineRun("PIPE-02", "etl_orders", 203, 12450, "SUCCESS"),
    PipelineRun("PIPE-03", "etl_products", 45, 891, "WARN"),
    PipelineRun("PIPE-04", "etl_events", 3782, 99103, "FAILED"),
]
total_rows = 0
count = 0
for run in runs:
    print(run)
    total_rows += run.rows_processed
    if run.is_success:
        count += 1
print(count)
print(f"{total_rows:,}")

