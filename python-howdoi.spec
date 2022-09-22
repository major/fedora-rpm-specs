%global srcname howdoi

Name:           python-%{srcname}
Version:        2.0.16
Release:        6%{?dist}
Summary:        Instant coding answers via the command line

License:        MIT
URL:            https://github.com/gleitz/howdoi
# pypi archive does not contain test data
# Source0:        {pypi_source}
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
Sherlock, your neighborhood command-line sloth sleuth.

Are you a hack programmer? Do you find yourself constantly Googling for how to
do basic programming tasks?

Suppose you want to know how to format a date in bash. Why open your browser and
read through blogs (risking major distraction) when you can simply stay in the
console and ask howdoi:

    $ howdoi format date bash
    > DATE=`date +%%Y-%%m-%%d`}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(appdirs)
BuildRequires:  python3dist(cachelib)
BuildRequires:  python3dist(keep)
BuildRequires:  python3dist(pygments)
BuildRequires:  python3dist(pyquery)

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version} -p1
# remove shebang
sed -i.shebang '1d' howdoi/howdoi.py
touch -r howdoi/howdoi.py.shebang howdoi/howdoi.py

%build
%py3_build

%install
%py3_install

%check
# some tests fail if run at once with
#   OSError: [Errno 24] Too many open files
# ``ulimit -n unlimited`` is not an option
TEST_CLASS=test_howdoi.py::HowdoiTestCase
skipped_tests=(multiple_answers position unicode_answer)
DESELECT=
for testcase in "${skipped_tests[@]}"; do
  DESELECT+=" --deselect ${TEST_CLASS}::test_${testcase}"
done
%pytest -v ${DESELECT}
for testcase in "${skipped_tests[@]}"; do
  SELECT+=" ${TEST_CLASS}::test_${testcase}"
done
%pytest -v ${SELECT}

%files -n python3-%{srcname}
%license LICENSE.txt
%doc CHANGES.txt README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/
%{_bindir}/%{srcname}


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 2.0.16-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 30 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.0.16-2
- Escape %%s in description
- fix shebang in non-executable file
- Use `--deselect` to temporarily skip expensive tests

* Tue Jun 29 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.0.16-1
- Initial package
