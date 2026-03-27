%global pypi_name cmd2

Name:             python-%{pypi_name}
Version:          2.5.11
Release:          %autorelease
Summary:          Extra features for standard library's cmd module

License:          MIT
URL:              https://pypi.python.org/pypi/cmd2
Source0:          %{pypi_source}
Patch0:           python-cmd2-2.5.11-disable-cov-tests.patch
# Adapted from https://github.com/python-cmd2/cmd2/pull/1419
Patch1:           Add-support-for-Python-3.14-and-remove-for-Python-3.8.patch
BuildArch:        noarch

%global _description\
Enhancements for standard library's cmd module.\
\
Drop-in replacement adds several features for command-prompt tools:\
\
 * Searchable command history (commands: "hi", "li", "run")\
 * Load commands from file, save to file, edit commands in file\
 * Multi-line commands\
 * Case-insensitive commands\
 * Special-character shortcut commands (beyond cmd's "@" and "!")\
 * Settable environment parameters\
 * Parsing commands with flags\
 * > (filename), >> (filename) redirect output to file\
 * < (filename) gets input from file\
 * bare >, >>, < redirect to/from paste buffer\
 * accepts abbreviated commands when unambiguous\
 * `py` enters interactive Python console\
 * test apps against sample session transcript (see example/example.py)\
\
Usable without modification anywhere cmd is used; simply import cmd2.Cmd\
in place of cmd.Cmd.\
\
See docs at http://packages.python.org/cmd2/

%description %_description

%package -n python3-cmd2
Summary:          %{summary}
BuildRequires:    python3-devel
BuildRequires:    python3-pytest
BuildRequires:    python3-pytest-mock
# An editor is needed for tests; vim works too
BuildRequires:    nano
Requires:         /usr/bin/which

%generate_buildrequires
%pyproject_buildrequires

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l cmd2

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md README.md docs

%changelog
%autochangelog
