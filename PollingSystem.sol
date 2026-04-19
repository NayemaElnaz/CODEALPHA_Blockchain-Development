// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract PollingSystem {
    struct Poll {
        string title;
        string[] options;
        uint256 endTime;
        mapping(uint256 => uint256) voteCount; // Option index => total votes
        mapping(address => bool) hasVoted;    // Track who voted in this poll
    }

    Poll[] public polls;

    // Create a new poll
    function createPoll(string memory _title, string[] memory _options, uint256 _durationInSeconds) public {
        Poll storage newPoll = polls.push();
        newPoll.title = _title;
        newPoll.options = _options;
        newPoll.endTime = block.timestamp + _durationInSeconds;
    }

    // Cast a vote
    function vote(uint256 _pollId, uint256 _optionIndex) public {
        Poll storage currentPoll = polls[_pollId];

        require(block.timestamp < currentPoll.endTime, "Voting has ended.");
        require(!currentPoll.hasVoted[msg.sender], "You have already voted.");
        require(_optionIndex < currentPoll.options.length, "Invalid option.");

        currentPoll.hasVoted[msg.sender] = true;
        currentPoll.voteCount[_optionIndex]++;
    }

    // Get winner after poll ends
    function getWinner(uint256 _pollId) public view returns (string memory winnerName, uint256 winnerVotes) {
        Poll storage currentPoll = polls[_pollId];
        require(block.timestamp >= currentPoll.endTime, "Poll is still active.");

        uint256 winningVoteCount = 0;
        uint256 winningOptionIndex = 0;

        for (uint256 i = 0; i < currentPoll.options.length; i++) {
            if (currentPoll.voteCount[i] > winningVoteCount) {
                winningVoteCount = currentPoll.voteCount[i];
                winningOptionIndex = i;
            }
        }

        return (currentPoll.options[winningOptionIndex], winningVoteCount);
    }
}