Name:           kalamine
Version:        0.38
Release:        %autorelease
Summary:        Cross-platform Keyboard Layout Maker
License:        MIT
URL:            https://github.com/OneDeadKey/kalamine
Source:         %{pypi_source kalamine}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-lxml


%description
A text-based, cross-platform Keyboard Layout Maker.


%prep
%autosetup
# rpmlint: E: zero-length
mv kalamine/generators/{__init.py__,__init__.py}
# rpmlint: E: non-executable-script
sed -e '1{/^#!/d}' -i kalamine/{__init__.py,cli*.py}
# remove Windows-only CLI
sed -e '/wkalamine/d' -i pyproject.toml


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l kalamine


%check
%{py3_test_envvars} %{python3} -m kalamine.cli build layouts/*.toml
%{py3_test_envvars} %{python3} -m kalamine.cli new test.toml
%pytest


%files -f %{pyproject_files}
%doc docs/*.md
%{_bindir}/kalamine
%{_bindir}/xkalamine


%changelog
%autochangelog
