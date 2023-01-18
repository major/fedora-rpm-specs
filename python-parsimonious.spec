Name:           python-parsimonious
Version:        0.10.0
Release:        %autorelease
Summary:        A fast pure-Python PEG parser

License:        MIT
URL:            https://github.com/erikrose/parsimonious
Source0:        %{url}/archive/%{version}/parsimonious-%{version}.tar.gz

BuildRequires:  python3-devel

BuildArch:      noarch

%description
Parsimonious aims to be the fastest arbitrary-lookahead parser written in pure
Python, and the most usable. It's based on parsing expression grammars (PEGs),
which means you feed it a simplified sort of EBNF notation. Parsimonious was
designed to undergird a MediaWiki parser that wouldn't take 5 seconds or a GB
of RAM to do one page, but it's applicable to all sorts of languages.

%prep
%autosetup -p 1 -n parsimonious-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files parsimonious

%check
%tox

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
