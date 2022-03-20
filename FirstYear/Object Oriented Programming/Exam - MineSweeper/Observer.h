//
// Created by Teo on 6/22/2021.
//

#ifndef E2_ALEXTEO24_OBSERVER_H
#define E2_ALEXTEO24_OBSERVER_H
#include <vector>
#include <algorithm>

/*
	Observer - Abstract class
	update method needs to be implemented by observers
*/
class Observer
{
public:
    virtual void update() = 0;
    virtual ~Observer() = default;
};


/*
	Observable or Subject - class that notifies changes in its state
	Derive from this class if you want to provide notifications
*/
class Observable
{
private:
    //Non-owning pointers to observer instances
    std::vector<Observer*> observers;
public:
    void addObserver(Observer *obs)
    {
        observers.push_back(obs);
    }

    void removeObserver(Observer *obs)
    {
        auto it = std::find(observers.begin(), observers.end(), obs);
        if (it != observers.end())
            observers.erase(it);
    }

    void notify()
    {
        for (auto obs: observers)
        {
            obs->update();
        }
    }
};
#endif //E2_ALEXTEO24_OBSERVER_H
