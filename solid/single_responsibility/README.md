# (S)ingle responsibility for every component. Component can be module/method/class

### Cohension and Coupling

- Cohension is degree to which each component is related to each other
- Coupling is the level of inter dependency between various component

### Reason to change(Solution for this is actually same as for the cohension and coupling)

- Each compoonent should only have one reason to change.
- If a component has multiple reason to change, there will be more frequency of change.
- An increase in frequency of change will only increase the chances of getting bugs.
- We should split components when there are multiple reasons to change.

### Summary
- Ask yourself what are the possible reasons for changing this component. Each reason for changing should be a single component unless there are very closely linked reasons.
- Aim for high conhension and loose coupling.(for lower code maintenance cost)
- Note: Do not create a huge number of classes. Combine the components if the responsibilities can be grouped in a sensible way.