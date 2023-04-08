Name:           python-hatchling
Version:        1.14.0
Release:        %autorelease
Summary:        The build backend used by Hatch

# SPDX
License:        MIT
URL:            https://pypi.org/project/hatchling
Source0:        %{pypi_source hatchling}
# Written for Fedora in groff_man(7) format based on --help output
Source100:      hatchling.1
Source200:      hatchling-build.1
Source300:      hatchling-dep.1
Source310:      hatchling-dep-synced.1
Source400:      hatchling-metadata.1
Source500:      hatchling-version.1

BuildArch:      noarch

BuildRequires:  python3-devel
# RHBZ#1985340, RHBZ#2076994
BuildRequires:  pyproject-rpm-macros >= 1.2.0

%global common_description %{expand:
This is the extensible, standards compliant build backend used by Hatch.}

%description %{common_description}


%package -n python3-hatchling
Summary:        %{summary}

%description -n python3-hatchling %{common_description}


%prep
%autosetup -n hatchling-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files hatchling

install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE100}' \
    '%{SOURCE200}' \
    '%{SOURCE300}' '%{SOURCE310}' \
    '%{SOURCE400}' \
    '%{SOURCE500}'


%check
# It’s not yet clear how, or if, we can run the upstream tests.
# https://github.com/pypa/hatch/issues/120
%pyproject_check_import


%files -n python3-hatchling -f %{pyproject_files}
%doc README.md

%{_bindir}/hatchling
%{_mandir}/man1/hatchling.1*
%{_mandir}/man1/hatchling-*.1*


%changelog
%autochangelog
