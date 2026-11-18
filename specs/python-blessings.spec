%bcond          tests 1
Summary:        Thin, practical wrapper around terminal coloring, styling, and positioning
Name:           python-blessings
Version:        1.7
Release:        %autorelease
License:        MIT
URL:            https://github.com/erikrose/blessings
Source:         %{pypi_source blessings}
# https://github.com/erikrose/blessings/issues/25
Patch:          0001-fix-tests-when-run-without-a-tty-fixes-25.patch
Patch:          0002-more-fixes-for-tests-without-a-tty.patch
# https://github.com/erikrose/blessings/pull/167
Patch:          0003-chore-replace-nose-with-pytest.patch
BuildArch:      noarch
%global _description %{expand:
Blessings lifts several of curses' limiting assumptions, and it makes your code
pretty, too:

* Use styles, color, and maybe a little positioning without necessarily
  clearing the whole screen first.
* Leave more than one screenful of scrollback in the buffer after your program
  exits, like a well-behaved command-line app should.
* Get rid of all those noisy, C-like calls to tigetstr and tparm, so your code
  does not get crowded out by terminal bookkeeping.
* Act intelligently when somebody redirects your output to a file, omitting the
  terminal control codes the user does not want to see (optional).}

%description %{_description}

%package -n     python3-blessings
Summary:        %{summary}
BuildRequires:  python3-devel
%description -n python3-blessings %{_description}

%prep
%autosetup -p1 -n blessings-%{version}

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-t}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files blessings

%check
%pyproject_check_import
%if %{with tests}
%tox
%endif

%files -n python3-blessings -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
