# when bootstrapping, we cannot yet use sphinx and pytest
# on RHEL, we don't need to build the documentation
%bcond docs %{undefined rhel}
%bcond tests 1

Name:           python-pygments
Version:        2.19.1
Release:        %autorelease
Summary:        Syntax highlighting engine written in Python

License:        BSD-2-Clause
URL:            https://pygments.org/
Source0:        %{pypi_source pygments}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-lxml
%if %{undefined rhel}
# this is only used in tests.contrast.test_contrasts
# to avoid pulling this package into RHEL, the test is ignored in %%check
BuildRequires:  python%{python3_pkgversion}-wcag-contrast-ratio
%endif
%endif
%if %{with docs}
BuildRequires:  make
BuildRequires:  python%{python3_pkgversion}-sphinx
# the sphinx config imports tests.contrast.test_contrasts:
BuildRequires:  python%{python3_pkgversion}-wcag-contrast-ratio
%endif


%global _description %{expand:
Pygments is a generic syntax highlighter suitable for use in code hosting,
forums, wikis or other applications that need to prettify source code.

Highlights are:

 * a wide range of over 500 languages and other text formats is supported
 * special attention is paid to details that increase highlighting quality
 * support for new languages and formats are added easily;
   most languages use a simple regex-based lexing mechanism
 * a number of output formats is available, among them HTML, RTF, LaTeX
   and ANSI sequences
 * it is usable as a command-line tool and as a library}

%description %_description


%package -n python%{python3_pkgversion}-pygments
Summary:        %{summary}
Provides:       pygmentize = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python%{python3_pkgversion}-pygments %_description


%prep
%autosetup -p1 -n pygments-%{version}

# Create pytest configuration to fix path resolution issues in pytest 8.4
# Upstream issue: https://github.com/pygments/pygments/issues/2992
cat > pytest.ini << EOF
[pytest]
collect_imported_tests = false
EOF

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pygments

install doc/pygmentize.1 -Dt %{buildroot}%{_mandir}/man1/

%if %{with docs}
%make_build -C doc html
rm doc/_build/html/.buildinfo
rm -rf doc/_build/html/_sources
chmod -x %{buildroot}%{_mandir}/man1/*.1
%endif


%if %{with tests}
%check
%pytest %{?rhel:--ignore tests/contrast/test_contrasts.py}
%endif


%files -n python%{python3_pkgversion}-pygments -f %{pyproject_files}
%doc AUTHORS CHANGES
%{?with_docs:%doc doc/_build/html}
%license LICENSE
%{_bindir}/pygmentize
%lang(en) %{_mandir}/man1/pygmentize.1*


%changelog
%autochangelog
