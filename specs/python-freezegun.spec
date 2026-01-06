%global modname freezegun
%global sum Let your Python tests travel through time

Name:               python-freezegun
Version:            1.5.5
Release:            %autorelease
Summary:            %{sum}

License:            Apache-2.0
URL:                https://pypi.io/project/freezegun
Source0:            https://pypi.io/packages/source/f/%{modname}/%{modname}-%{version}.tar.gz

Patch:              freezegun-1.5.1-no-coverage.patch

BuildArch:          noarch

%description
freezegun is a library that allows your python tests to travel through time by
mocking the datetime module.


%package -n python3-freezegun
Summary:            %{sum}

BuildRequires:      python3-devel

%{?python_provide:%python_provide python3-freezegun}

#Requires:           python3-six
#Requires:           python3-dateutil >= 2.7

%description -n python3-freezegun
freezegun is a library that allows your python tests to travel through time by
mocking the datetime module. This is the Python 3 library.

%prep
%autosetup -p1 -n %{modname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l freezegun

%check
# Ignore two tests that are broken when run on systems in certain timezones.
# Reported upstream: https://github.com/spulec/freezegun/issues/348
pytest-3 --deselect tests/test_datetimes.py::TestUnitTestMethodDecorator::test_method_decorator_works_on_unittest_kwarg_frozen_time \
         --deselect tests/test_datetimes.py::TestUnitTestMethodDecorator::test_method_decorator_works_on_unittest_kwarg_hello

%files -n python3-freezegun -f %{pyproject_files}
%doc README.rst LICENSE

%changelog
%autochangelog
