Name:           python-pyrankvote
Version:        2.0.6
Release:        %autorelease
Summary:        Library for different ranked voting methods

License:        MIT
URL:            https://github.com/jontingvold/pyrankvote
Source:         %{url}/archive/v%{version}/pyrankvote-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# Tests
BuildRequires:  python3dist(pytest)

# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
PyRankVote is a python library for different ranked-choice voting systems
(sometimes called preferential voting systems) created by Jon Tingvold in June
2019.

The following ranking methods are implemented for electing one person/
alternative (e.g. electing the chairman to a board):

Instant-runoff voting (IRV)—often known as the alternative vote
The following ranking methods are implemented for electing multiple
people/alternatives (e.g. electing board members):

- Single transferable vote (STV)—generally preferred
- Preferential block voting (PBV)
- Different ranking methods
- Instant runoff voting (IRV) is a single candidate election method that elects
  the candidate that can obtain majority support (more than 50%).

Voters rank candidates and are granted one vote. The candidate with fewest
votes is removed and this candidate's votes are transferred according to the
voters 2nd preference (or 3rd etc).

Preferential block voting (PBV) is a multiple candidate election method that
elects candidates that can obtain majority support (more than 50%). PBV tends
to elect uncontroversial candidates that agree with each other. Minority group
often lose their representation.

Voters rank candidates and are granted as many votes as there are people that
should be elected. The candidate with fewest votes are removed and this
candidate's votes are transferred according to the voters 2nd preference
(or 3rd etc).

Single transferable vote (STV) is a multiple candidate election method that
elects candidates based on proportional representation. Minority (and extreme)
groups get representation if they have enough votes to elect a candidate. STV
is therefore the preferred ranked-choice voting method for parliament elections
and most multiple seat elections, but it's more complex than PBV, so it
explained last.

Voters rank candidates and are granted as one vote each. If a candidate gets
more votes than the threshold for being elected, the candidate is proclaimed as
winner. This function uses the Droop quota, where

  droop_quota = votes/(seats+1) + 1

If one candidate gets more votes than the threshold the excess votes are
transferred to voters that voted for this candidate's 2nd (or 3rd, 4th, etc)
alternative. If no candidate gets over the threshold, the candidate with fewest
votes is removed. Votes for this candidate is then transferred to voters 2nd
(or 3rd, 4th, etc) alternative.

Preferential block voting and Single transferable vote are the same as
Instant-runoff voting when only one candidate is elected.

Instant-runoff voting and Preferential block voting are basically the same as
exhaustive ballot, the preferred method in Rober's rules of order. The only
difference is that in exhaustive ballot voters can adjust their preferences
between each round (elimination or election of one candidate).}

%description %_description

%package -n     python3-pyrankvote
Summary:        %{summary}

%description -n python3-pyrankvote %_description


%prep
%autosetup -p1 -n pyrankvote-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files -l pyrankvote


%check
%pyproject_check_import
%pytest

%files -n python3-pyrankvote -f %{pyproject_files}
%license LICENSE.txt
%doc README.md
%doc examples.py

%changelog
%autochangelog
