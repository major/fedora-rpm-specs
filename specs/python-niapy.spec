Name:           python-niapy
Version:        2.6.1
Release:        %autorelease
Summary:        Micro framework for building nature-inspired algorithms

License:        MIT
URL:            https://github.com/NiaOrg/NiaPy
Source:         %{url}/archive/v%{version}/NiaPy-%{version}.tar.gz

# Tidy up some minutiae in the examples
#
# Remove executable permissions from examples/run_all.sh: it does not have a
# shebang line, so having the execute bit set is useless.
#
# Convert examples/run_loa form CRLF line terminations (DOS/Windows style) to
# UNIX-style, to match the other files in the project.
#
# https://github.com/NiaOrg/NiaPy/pull/742
Patch:          %{url}/pull/742.patch

BuildSystem:            pyproject
BuildOption(install):   -L niapy

BuildArch:      noarch

# setup.py: tests_require (also includes unwanted coverage/linting/etc. deps.)
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
BuildRequires:  %{py3_dist pytest}

%global _description %{expand:
Nature-inspired algorithms are a very popular tool for solving optimization
problems. Numerous variants of nature-inspired algorithms have been developed
since the beginning of their era. To prove their versatility, those were tested
in various domains on various applications, especially when they are
hybridized, modified or adapted. However, implementation of nature-inspired
algorithms is sometimes a difficult, complex and tedious task. In order to
break this wall, NiaPy is intended for simple and quick use, without spending
time for implementing algorithms from scratch.}

%description %_description

%package -n python3-niapy
Summary:        %{summary}

# The -doc subpackage was merged into python3-niapy for simplicity.
Provides:       python-niapy-doc = %{version}-%{release}
Obsoletes:      python-niapy-doc < 2.5.2-10

%description -n python3-niapy %_description

%prep
%autosetup -n NiaPy-%{version} -p1

# - Don’t bound the version of Python. We must use the system interpreter.
# - Convert SemVer pins to minimum versions, since we can’t generally respect
#   the upper bounds in Fedora.
sed -r -i -e 's/^python ?=/# &/' -e 's/([^#]+ ?= ?")\^/\1>=/' pyproject.toml

%check -a
%pytest -ra -k "${k-}"

%files -n python3-niapy -f %{pyproject_files}
%license LICENSE
%doc Algorithms.md
%doc CHANGELOG.md
%doc CITATION.cff
%doc Problems.md
%doc README.md
%doc examples/
%doc paper/

%changelog
%autochangelog
