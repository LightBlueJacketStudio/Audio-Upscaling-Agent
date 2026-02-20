1/31/2026
---
Today I got the split audio working by calling spleeter library.<br>
I encountered a weird situation at first when the script is not conatined in a main(), when I try to run the script it would fall into an infinite loop.<br>
I did some search on ChatGPT, and it turns out that is was a Windows-specific problem because when multiprocessing is enabled on Windows, the script itself got re-imported.<br>
"multiprocessing starts new worker processes by re-importing your script.
Spleeter’s Separator() creates a Pool() internally (self._pool = Pool()), so when the child process re-imports your script, it hits Separator() again… which spawns more processes…" (chatGPT) and so by guard teh script in main, and added these lines 
```
if __name__ == "__main__":
    # Only needed on Windows when multiprocessing is used (Spleeter uses it internally)
    import multiprocessing as mp
    mp.freeze_support()
    main()
```

It prevents the script from re-running itself endlessly.<br>
Overall, I think the initial separation is OK.


2/6/2026
done with standardizing before input to spleeter
use "pip freeze requirement.txt"
to do requirement document

2/19/2026
done with visualization. comparing the preprocessed audio and post-processed audio
we observed that the standardization does make some visible change to the audio, some peaks that was previously capped was kinda restored.
