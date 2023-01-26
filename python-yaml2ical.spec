%global pypi_name yaml2ical

%global common_description %{expand:
yaml2ical converts a series of meeting descriptions in YAML format
into one or several .ics files suitable for calendaring. It checks for
scheduling conflicts in specific locations.}

Name:           python-%{pypi_name}
Version:        0.13.0
Release:        %autorelease
Summary:        Convert YAML meeting descriptions into iCalendar files

License:        Apache-2.0
URL:            https://opendev.org/opendev/yaml2ical
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  sed
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description
%{common_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{common_description}

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove unnecessary shebang
sed -e '\|#!/usr/bin/env python|d' -i yaml2ical/tests/sample_data.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
# https://storyboard.openstack.org/#!/story/2010548
%pytest --deselect=yaml2ical/tests/test_meeting.py::MeetingTestCase::test_skip_meeting

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/yaml2ical

%changelog
%autochangelog
