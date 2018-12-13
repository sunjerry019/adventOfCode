// prog.cpp
// Copyright (c) 2017, zhiayang@gmail.com
// Licensed under the Apache License Version 2.0.


#include "assert.h"

#include <map>
#include <set>
#include <stack>
#include <array>
#include <deque>
#include <string>
#include <vector>
#include <unordered_set>

#include "utils.h"
#include "tinyformat.h"

int main()
{
	std::vector<std::pair<char, char>> input = {
		{'G', 'M'},
		{'T', 'E'},
		{'P', 'M'},
		{'V', 'L'},
		{'Y', 'B'},
		{'K', 'Z'},
		{'H', 'I'},
		{'D', 'U'},
		{'C', 'L'},
		{'R', 'Z'},
		{'U', 'B'},
		{'J', 'M'},
		{'M', 'E'},
		{'I', 'X'},
		{'N', 'O'},
		{'S', 'F'},
		{'X', 'A'},
		{'F', 'Q'},
		{'B', 'Z'},
		{'Q', 'W'},
		{'L', 'W'},
		{'O', 'Z'},
		{'A', 'Z'},
		{'E', 'W'},
		{'W', 'Z'},
		{'G', 'R'},
		{'H', 'A'},
		{'A', 'W'},
		{'Y', 'D'},
		{'O', 'A'},
		{'V', 'U'},
		{'H', 'W'},
		{'K', 'F'},
		{'J', 'X'},
		{'V', 'R'},
		{'Q', 'A'},
		{'F', 'B'},
		{'G', 'P'},
		{'L', 'A'},
		{'B', 'Q'},
		{'H', 'J'},
		{'J', 'L'},
		{'F', 'E'},
		{'U', 'A'},
		{'G', 'Q'},
		{'G', 'S'},
		{'K', 'J'},
		{'N', 'B'},
		{'F', 'O'},
		{'C', 'Z'},
		{'B', 'E'},
		{'M', 'S'},
		{'A', 'E'},
		{'E', 'Z'},
		{'K', 'I'},
		{'P', 'A'},
		{'Y', 'L'},
		{'Y', 'J'},
		{'G', 'N'},
		{'Q', 'L'},
		{'D', 'X'},
		{'C', 'I'},
		{'K', 'B'},
		{'N', 'F'},
		{'D', 'M'},
		{'B', 'A'},
		{'U', 'J'},
		{'Q', 'Z'},
		{'X', 'F'},
		{'K', 'X'},
		{'U', 'E'},
		{'X', 'W'},
		{'K', 'Q'},
		{'I', 'E'},
		{'D', 'J'},
		{'P', 'I'},
		{'K', 'D'},
		{'S', 'X'},
		{'C', 'R'},
		{'P', 'W'},
		{'I', 'O'},
		{'S', 'O'},
		{'K', 'C'},
		{'N', 'Q'},
		{'L', 'E'},
		{'L', 'Z'},
		{'K', 'W'},
		{'Y', 'A'},
		{'L', 'O'},
		{'N', 'W'},
		{'R', 'W'},
		{'C', 'O'},
		{'H', 'X'},
		{'V', 'Y'},
		{'S', 'W'},
		{'V', 'E'},
		{'Q', 'E'},
		{'P', 'H'},
		{'V', 'H'},
		{'N', 'Z'},
		{'C', 'A'}

		// {'A', 'N'},
		// {'P', 'R'},
		// {'O', 'T'},
		// {'J', 'U'},
		// {'M', 'X'},
		// {'E', 'X'},
		// {'N', 'T'},
		// {'W', 'G'},
		// {'Z', 'D'},
		// {'F', 'Q'},
		// {'U', 'L'},
		// {'I', 'X'},
		// {'X', 'Y'},
		// {'D', 'Y'},
		// {'S', 'K'},
		// {'C', 'G'},
		// {'K', 'V'},
		// {'B', 'R'},
		// {'Q', 'L'},
		// {'T', 'H'},
		// {'H', 'G'},
		// {'V', 'L'},
		// {'L', 'R'},
		// {'G', 'Y'},
		// {'R', 'Y'},
		// {'G', 'R'},
		// {'X', 'V'},
		// {'V', 'Y'},
		// {'Z', 'U'},
		// {'U', 'R'},
		// {'J', 'Y'},
		// {'Z', 'C'},
		// {'O', 'L'},
		// {'C', 'H'},
		// {'V', 'G'},
		// {'F', 'K'},
		// {'Q', 'G'},
		// {'S', 'Q'},
		// {'M', 'G'},
		// {'T', 'L'},
		// {'C', 'Q'},
		// {'T', 'V'},
		// {'W', 'Z'},
		// {'C', 'K'},
		// {'I', 'C'},
		// {'X', 'Q'},
		// {'F', 'X'},
		// {'J', 'S'},
		// {'I', 'K'},
		// {'U', 'Q'},
		// {'I', 'Q'},
		// {'N', 'H'},
		// {'A', 'T'},
		// {'T', 'G'},
		// {'D', 'T'},
		// {'A', 'X'},
		// {'D', 'G'},
		// {'C', 'T'},
		// {'W', 'Q'},
		// {'W', 'K'},
		// {'V', 'R'},
		// {'H', 'R'},
		// {'F', 'H'},
		// {'F', 'V'},
		// {'U', 'T'},
		// {'K', 'H'},
		// {'B', 'T'},
		// {'H', 'Y'},
		// {'J', 'Z'},
		// {'B', 'Y'},
		// {'I', 'V'},
		// {'W', 'V'},
		// {'Q', 'R'},
		// {'I', 'S'},
		// {'E', 'H'},
		// {'J', 'B'},
		// {'S', 'G'},
		// {'E', 'S'},
		// {'N', 'I'},
		// {'Z', 'F'},
		// {'E', 'I'},
		// {'S', 'B'},
		// {'D', 'L'},
		// {'Q', 'T'},
		// {'Q', 'H'},
		// {'K', 'Y'},
		// {'M', 'U'},
		// {'U', 'K'},
		// {'W', 'I'},
		// {'J', 'W'},
		// {'K', 'T'},
		// {'P', 'Y'},
		// {'L', 'G'},
		// {'K', 'B'},
		// {'I', 'Y'},
		// {'U', 'B'},
		// {'P', 'O'},
		// {'O', 'W'},
		// {'O', 'J'},
		// {'A', 'J'},
		// {'F', 'G'}
	};

	struct letter_t
	{
		char letter;
		std::vector<letter_t*> dependsOn;

		bool satisfied = false;
	};

	#define NUM_LETTERS 26

	std::vector<letter_t> letters;
	for(int i = 0; i < NUM_LETTERS; i++)
	{
		auto l = letter_t();
		l.letter = 'A' + i;

		letters.push_back(l);
	}


	for(const auto& k : input)
	{
		// second depends on first.
		letters[k.second - 'A'].dependsOn.push_back(&letters[k.first - 'A']);
	}


	// see which ones are available!
	std::string final_order;
	{
		while(true)
		{
			bool changed = false;
			for(int i = 0; i < NUM_LETTERS; i++)
			{
				auto& let = letters[i];
				if(!let.satisfied)
				{
					// check all dependencies

					bool sats = true;
					for(auto dep : let.dependsOn)
						sats = sats && dep->satisfied;

					let.satisfied = sats;
					if(let.satisfied)
					{
						changed = true;
						final_order.push_back(let.letter);

						break;
					}
				}
			}

			if(!changed) break;
		}

		tfm::printfln("part 1: %s", final_order);
	}



	// reset
	for(auto& let : letters)
		let.satisfied = false;


	{
		struct worker_t
		{
			char working_on = 0;
			int time_left = 0;
		};

		#define NUM_WORKERS 5
		#define MIN_WORK_TIME 60

		std::deque<char> queue;
		std::deque<char> already_queued;
		std::array<worker_t, NUM_WORKERS> workers = { };

		std::string done;

		auto reduce_unemployment = [&workers, &queue, &letters, &done]() {
			for(size_t i = 0; i < NUM_WORKERS; i++)
			{
				if(workers[i].working_on == 0 && queue.size() > 0)
				{
					auto let = queue.front();
					queue.pop_front();

					workers[i].working_on = let;
					workers[i].time_left = 1 + MIN_WORK_TIME + (let - 'A');
				}
			}
		};

		auto tick_workers = [&workers, &queue, &letters, &done, &reduce_unemployment]() {
			reduce_unemployment();

			for(size_t i = 0; i < NUM_WORKERS; i++)
			{
				if(workers[i].time_left == 1 && workers[i].working_on != 0)
				{
					auto let = &letters[workers[i].working_on - 'A'];
					let->satisfied = true;
					workers[i].working_on = 0;

					done.push_back(let->letter);


					// see if there's more shit to do!
					if(queue.size() > 0)
					{
						auto let = queue.front();
						queue.pop_front();

						workers[i].working_on = let;
						workers[i].time_left = 1 + MIN_WORK_TIME + (let - 'A');
					}
				}
				else if(workers[i].working_on != 0)
				{
					workers[i].time_left--;
				}
			}
		};

		int tick = 0;
		tfm::printfln("tick    w1    w2    done        queue");
		while(true)
		{
			for(int i = 0; i < NUM_LETTERS; i++)
			{
				auto let = &letters[i];
				if(!let->satisfied)
				{
					// check all dependencies
					bool sats = true;
					for(auto dep : let->dependsOn)
						sats = sats && dep->satisfied;

					if(sats && std::find(already_queued.begin(), already_queued.end(), let->letter) == already_queued.end())
					{
						queue.push_back(let->letter);
						already_queued.push_back(let->letter);
						// tfm::printfln("add %c to queue!", let->letter);
						// reduce_unemployment();
						// break;
					}
				}
			}

			std::string q;
			for(auto l : queue)
				q += l;

			tfm::printfln("%4d    %c     %c     %-*s      %s", tick, workers[0].working_on, workers[1].working_on, NUM_LETTERS, done, q);

			tick_workers(); tick++;

			if(done.length() == NUM_LETTERS) break;
		}

		tfm::printfln("part 2: took %d ticks (%s)", tick, done);
	}
}
