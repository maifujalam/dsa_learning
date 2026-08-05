1. Difference between reservation and saving plan and spot instances in AWS?
    Reservation: A reservation is a commitment to purchase a specific amount of EC2 capacity for a fixed period of time, 
    typically one or three years.But we have to stick with the same instance type and size for the entire reservation period.

    Saving Plan: A saving plan is a flexible commitment to use a specific amount of EC2 compute time over a one-year period.We can choose instance of different instance type of the same instance family.
    move from t3a.medium to t3a.large, for example, and still receive the same discount. Saving plans offer more flexibility than reservations, as they allow you to change instance types and sizes within the same family.
    
    Spot Instances: Spot instances are unused EC2 capacity that you can bid on at significantly lower prices than on-demand instances. However, they can be terminated at any time if the spot price exceeds your bid.