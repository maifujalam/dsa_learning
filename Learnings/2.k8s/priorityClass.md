1. Whats priority class?
priorityClass is a cluster wide kubernetes object which maps a priority name ot integer value.
Higher the number higher the priority.
Pod with higher priority class value are scheduled faster.
It may evict the low resource pod if it crosses its priority class value.During resourcs cunch.
