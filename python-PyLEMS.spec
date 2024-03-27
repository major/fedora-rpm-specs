# Require network, so run locally on mock with --enable-network
%bcond_with tests

%global forgeurl https://github.com/LEMS/pylems/

%global _description \
A LEMS (http://lems.github.io/LEMS) simulator written in Python which can be \
used to run NeuroML2 (http://neuroml.org/neuroml2.php) models.


Name:           python-PyLEMS
Version:        0.6.7
Release:        %autorelease
Summary:        LEMS interpreter implemented in Python

%forgemeta

License:        LGPL-3.0-only

# Use github source. Pypi source does not include license and examples.
URL:            %{forgeurl}
Source0:        %{forgesource}
# Generate man page for pylems
# help2man -n "LEMS interpreter implemented in Python" --version-string="0.5.9" -N pylems -S "https://lems.github.io" -o pylems.1
# Sent upstream: https://github.com/LEMS/pylems/pull/64

BuildArch:      noarch

%description
%{_description}

%package -n python3-PyLEMS
Summary:        %{summary}
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

%description -n python3-PyLEMS
%{_description}

%package doc
Summary: %{summary}

%description doc
%{_description}


%prep
%forgeautosetup

# remove shebang
sed -i '1d' lems/dlems/exportdlems.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l lems

install -p -m 0644 -D -t $RPM_BUILD_ROOT/%{_mandir}/man1/  man/man1/*.1

%check
%if %{with tests}
# A lot of the tests use files from other software repositories, so we can't use them.
%{pytest}
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} examples/apitest.py
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} examples/apitest2.py
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} examples/loadtest.py
%endif

%files -n python3-PyLEMS -f %{pyproject_files}
%{_bindir}/pylems
%{_mandir}/man1/pylems.1*

%files doc
%license LICENSE.lesser
%doc README.md examples

%changelog
%autochangelog
