# How to


First of all instal Data Version Control LTS
```
$ sudo snap install dvc --classic
```

Clone the repository
```
git clone git@github.com:itsmeale/dvc-first-steps.git
```

Pull the project raw data (this only will work if you have my GCS credentials, but I'm putting this step just to show how easy can be reproductibility with DVC)
```
dvc pull
```

Reproduce the prepare and train pipeline with
```
dvc repro 
```

# Next steps
- [ ] Add metrics visualization when finishes the train process