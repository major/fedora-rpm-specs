Name:           python-pyspellchecker
Version:        0.8.1
Release:        %autorelease
Summary:        Pure python spell checker based on work by Peter Norvig

License:        MIT
URL:            https://github.com/barrust/pyspellchecker
Source:         %{url}/archive/v%{version}/pyspellchecker-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
pyspellchecker (Pure Python Spell Checking) uses a Levenshtein Distance
algorithm to find permutations within an edit distance of 2 from the original
word. It then compares all permutations (insertions, deletions, replacements,
and transpositions) to known words in a word frequency list. Those words that
are found more often in the frequency list are more likely the correct results.

pyspellchecker supports multiple languages including English, Spanish, German,
French, Portuguese, Arabic and Basque. For information on how the dictionaries
were created and how they can be updated and improved, please see the Dictionary
Creation and Updating section of the readme!

pyspellchecker allows for the setting of the Levenshtein Distance (up to two) to
check. For longer words, it is highly recommended to use a distance of 1 and not
the default 2. See the quickstart to find how one can change the distance
parameter.}

%description %_description

%package -n     python3-pyspellchecker
Summary:        %{summary}

%description -n python3-pyspellchecker %_description

%prep
%autosetup -p1 -n pyspellchecker-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files spellchecker

%check
%pytest

%files -n python3-pyspellchecker -f %{pyproject_files}


%changelog
%autochangelog
