%global srcname howdoi

Name:           python-%{srcname}
Version:        2.0.20
Release:        %autorelease
Summary:        Instant coding answers via the command line

License:        MIT
URL:            https://github.com/gleitz/howdoi
# pypi archive does not contain test data
# Source0:        {pypi_source}
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

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


%package -n %{srcname}
Summary:        %{summary}
Provides:       python3-%{srcname} = %{version}-%{release}
Obsoletes:      python3-%{srcname} < 2.0.20-2

%description -n %{srcname} %_description


%prep
%autosetup -n %{srcname}-%{version} -p1
# remove shebang
sed -i.shebang '1d' howdoi/howdoi.py
touch -r howdoi/howdoi.py.shebang howdoi/howdoi.py

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files %srcname


%check
TEST_CLASS=test_howdoi.py::HowdoiTestCase
skipped_tests=(colorize)
DESELECT=
for testcase in "${skipped_tests[@]}"; do
  DESELECT+=" --deselect ${TEST_CLASS}::test_${testcase}"
done
%pytest -v ${DESELECT}


%files -n %{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc CHANGES.txt README.md
%{_bindir}/%{srcname}


%changelog
%autochangelog
