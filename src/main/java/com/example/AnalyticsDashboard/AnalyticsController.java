package com.example.AnalyticsDashboard;

import org.springframework.web.bind.annotation.*;
import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("/api")
public class AnalyticsController {
    private final List<AnalyticsEntry> entries = new ArrayList<>();

    @PostMapping("/analytics")
    public AnalyticsEntry addEntry(@RequestBody AnalyticsEntry entry) {
        entries.add(entry);
        return entry;
    }

    @GetMapping("/analytics")
    public List<AnalyticsEntry> getAnalytics() {
        return entries;
    }
}