Name:           python-sure
Version:        2.0.1
Release:        %autorelease
Summary:        Idiomatic assertion toolkit with human-friendly failure messages

License:        GPL-3.0-or-later
URL:            https://github.com/gabrielfalcao/sure
Source0:        %{url}/archive/%{version}/sure-%{version}.tar.gz

# Trivial downstream man page for (nearly pointless) executable
Source1:        sure.1

# Python 3.10 workaround
# In test_context_is_not_optional(), only check the exception type
# https://github.com/gabrielfalcao/sure/issues/169
Patch:          python3.10-workaround.patch

# Drop PyPI mock dependency; use unittest.mock instead
# https://github.com/gabrielfalcao/sure/pull/188
# https://discussion.fedoraproject.org/t/f40-change-proposal-remove-python-mock-useage-system-wide/100082
Patch:          %{url}/pull/188.patch

BuildArch:      noarch

BuildRequires:  python3-devel

# TODO: remove mock dependency from install_requires
# https://fedoraproject.org/wiki/Changes/DeprecatePythonMock
# https://github.com/gabrielfalcao/sure/pull/161

# Test dependencies
# development.txt: pytest==6.2.4
BuildRequires:  python3dist(pytest)

%global common_description %{expand:
An idiomatic testing library for python with powerful and flexible assertions
created by Gabriel Falcão. Sure’s developer experience is inspired and modeled
after RSpec Expectations and should.js.}

%description %{common_description}


%package -n python3-sure
Summary:        %{summary}

Obsoletes:      python-sure-doc < 2.0.1-9

%description -n python3-sure %{common_description}


%prep
%autosetup -p1 -n sure-%{version}

# Do not generate a coverage report; this obviates the BR on pytest-cov
sed -r -i 's/[[:blank:]]--cov=[^[:blank:]]+//' setup.cfg


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l sure

install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE1}'


%check
# The old_api tests use python3dist(nose), which is deprecated and which we
# have removed from the BuildRequires:
# https://fedoraproject.org/wiki/Changes/DeprecateNose
%pytest --ignore=tests/test_old_api.py


%files -n python3-sure -f %{pyproject_files}
%doc CHANGELOG.md README.rst TODO.rst
%{_bindir}/sure
%{_mandir}/man1/sure.1*


%changelog
%autochangelog
