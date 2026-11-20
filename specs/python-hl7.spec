Name:           python-hl7
Version:        0.4.5
Release:        %autorelease
Summary:        Python library parsing HL7 v2.x messages

License:        BSD-3-Clause
URL:            https://github.com/johnpaulett/python-hl7
Source0:        %{pypi_source hl7}
# Use intersphinx references from Fedora python documentation subpackage
Patch:          docs-intersphinx.patch
# Remove build status logo that is no longer available in the repository
# https://github.com/johnpaulett/python-hl7/pull/87
Patch:          remove-build-status-logo.patch

BuildArch:      noarch
BuildRequires:  python3-devel
# Documentation requirements
BuildRequires:  texinfo
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx-theme-alabaster
# Intersphinx references
BuildRequires:  python3-docs

%global _description %{expand:
python-hl7 is a simple library for parsing messages of Health Level 7 (HL7)
version 2.x into Python objects. python-hl7 includes a simple client that can
send HL7 messages to a Minimal Lower Level Protocol (MLLP) server (mllp_send).

HL7 is a communication protocol and message format for health care data. It is
the de-facto standard for transmitting data between clinical information
systems and between clinical devices. The version 2.x series, which is often is
a pipe delimited format is currently the most widely accepted version of HL7
(there is an alternative XML-based format).}

%description %_description

%package -n     python3-hl7
Summary:        %{summary}

%description -n python3-hl7 %_description


%prep
%autosetup -p1 -n hl7-%{version}

cp %{_docdir}/python3-docs/html/objects.inv docs/

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

pushd docs
sphinx-build . build -b texinfo
pushd build
makeinfo --docbook python-hl7.texi
popd
popd

%install
%pyproject_install
%pyproject_save_files -l hl7


mkdir -p %{buildroot}%{_datadir}/help/en/hl7
install -m644 docs/build/python-hl7.xml %{buildroot}%{_datadir}/help/en/hl7

%check
%pyproject_check_import
%{py3_test_envvars} %{python3} -m unittest discover -t . -s tests

%files -n python3-hl7 -f %{pyproject_files}
%{_bindir}/mllp_send
%doc README.rst
%lang(en) %{_datadir}/help/en/hl7

%changelog
%autochangelog
