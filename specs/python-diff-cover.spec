%global desc Diff coverage is the percentage of new or modified lines that are covered by \
tests. This provides a clear and achievable standard for code review: If you \
touch a line of code, that line should be covered. Code coverage is *every* \
developer's responsibility! \
\
The diff-cover command line tool compares an XML coverage report with the \
output of git diff. It then reports coverage information for lines in the \
diff.

Name:           python-diff-cover
Version:        10.5.1
Release:        %autorelease
BuildArch:      noarch

License:        Apache-2.0
Summary:        Automatically find diff lines that need test coverage
URL:            https://github.com/Bachmann1234/diff-cover
Source0:        %{url}/archive/v%{version}/diff-cover-%{version}.tar.gz

BuildRequires: help2man
BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: python3-pytest-mock
BuildRequires: python3-pytest-datadir

%description
%{desc}

%package -n python3-diff-cover
Summary:        %{summary}
Requires:       git

%description -n python3-diff-cover
%{desc}

%prep
%autosetup -n diff_cover-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
mkdir -p %{buildroot}%{_mandir}/man1
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    help2man --no-info --version-string 'diff-cover %{version}' \
        -o %{buildroot}%{_mandir}/man1/diff-cover.1 \
        %{buildroot}%{_bindir}/diff-cover

PYTHONPATH=%{buildroot}%{python3_sitelib} \
    help2man --no-info --version-string 'diff-quality %{version}' \
        -o %{buildroot}%{_mandir}/man1/diff-quality.1 \
        %{buildroot}%{_bindir}/diff-quality
%pyproject_save_files diff_cover

%check
%pyproject_check_import

# disable code quality checker tests, but run the rest.
%pytest -k 'not TestDiffQualityIntegration and not TestFlake8QualityReporterTest'

%files -n python3-diff-cover -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_mandir}/man1/diff-cover.1*
%{_mandir}/man1/diff-quality.1*
%{_bindir}/diff-cover
%{_bindir}/diff-quality

%changelog
%autochangelog
