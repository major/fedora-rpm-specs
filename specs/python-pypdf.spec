# docs require myst_parser and python3-docs, not in RHEL
%bcond docs %[%{undefined rhel} || %{defined epel}]
# fonts support requires fonttools, buildroot only in RHEL
# image support requires Pillow, not in RHEL
%bcond extras %[%{undefined rhel} || %{defined epel}]
# tests require Pillow, pytest-socket, and pytest-timeout, not in RHEL
%bcond tests %[%{undefined rhel} || %{defined epel}]

%global srcname pypdf
%global forgeurl https://github.com/py-pdf/pypdf

Name:           python-%{srcname}
Version:        6.16.1
Release:        %autorelease
Summary:        Pure-Python PDF library

License:        BSD-3-Clause
URL:            https://pypdf.readthedocs.io
# PyPI tarball doesn't include tests
Source:         %{forgeurl}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with docs}
BuildRequires:  python3-docs
BuildRequires:  sed
%endif
%if %{with tests}
# Test dependencies added manually since pyproject.toml doesn't specify them
# separately from dev dependencies.
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-socket)
BuildRequires:  python3dist(pytest-timeout)
%endif

%global _description %{expand:
pypdf is a free and open-source pure-python PDF library capable of splitting,
merging, cropping, and transforming the pages of PDF files. It can also add
custom data, viewing options, and passwords to PDF files. pypdf can retrieve
text and metadata from PDFs as well.}

%description %_description

%package -n     python3-pypdf
Summary:        %{summary}

%description -n python3-pypdf %_description

%if %{with extras}
%pyproject_extras_subpkg -n python3-pypdf crypto,fonts,image,full
%endif

%if %{with docs}
%package        doc
Summary:        Documentation for %{name}
Requires:       python3-docs

%description    doc
This package provides additional documentation for %{name}.
%endif

%prep
%autosetup -p1 -n %{srcname}-%{version}

# Fedora currently doesn't provide python-bidi nor arabic-reshaper, so drop the
# optional RTL (Arabic/Hebrew) text shaping support: the "rtl_text" extra,
# and its two entries in the "full" extra.
# Note that pypdf degrades gracefully,
# pypdf.generic._appearance_stream.HAS_RTL_SUPPORT becomes False.
sed -i -e '/^rtl_text = \[$/,/^\]$/d' \
       -e '/^ *"arabic-reshaper",$/d' \
       -e '/^ *"python-bidi"$/d' \
       pyproject.toml
# Fail loudly rather than silently shipping broken dependencies if upstream
# reformats the extras in a future release.
if grep -qE 'arabic-reshaper|python-bidi' pyproject.toml; then
    echo 'ERROR: RTL extras removal failed, update the sed expressions above' >&2
    exit 1
fi

%if %{with docs}
# Use local intersphinx inventory
sed -r \
    -e 's|https://docs.python.org/\{python_version\}|%{_docdir}/python3-docs/html|' \
    -i docs/conf.py
%endif

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x crypto,fonts,image,full} %{?with_docs:-x docs}

%build
%pyproject_wheel

%if %{with docs}
# Build docs
sphinx-build-3 docs html
rm -rf html/{.buildinfo,.doctrees}
%endif

%install
%pyproject_install
%pyproject_save_files --assert-license %{srcname}

%check
%pyproject_check_import
%if %{with tests}
# Deselect tests downloading files from external hosts and tests requiring
# sample files which are not included in the source tarball.
# Additionally, deselect the test_appearance_stream_rtl test which tests the
# reshaped/reordered RTL output and has no guard for missing
# python-bidi/arabic-reshaper, which are dropped in %%prep.
%pytest -m "not enable_socket and not samples" \
    --deselect tests/test_appearance_stream.py::test_appearance_stream_rtl
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG.md CONTRIBUTORS.md

%if %{with docs}
%files doc
%license LICENSE
%doc html
%endif

%changelog
%autochangelog

