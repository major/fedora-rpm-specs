
%global upstream_version 1.4

Name:           rpmdeplint
Version:        1.4
Release:        29%{?dist}
Summary:        Tool to find errors in RPM packages in the context of their dependency graph
License:        GPLv2+
URL:            https://pagure.io/rpmdeplint
Source0:        https://files.pythonhosted.org/packages/source/r/%{name}/%{name}-%{upstream_version}.tar.gz
Patch0:         0001-Hotfix-for-libdnf-in-Fedora-29.patch
Patch1:         0001-Silence-some-Deprecation-warnings.patch
Patch2:         0001-Decode-rpm_file-rpm.RPMTAG_ARCH-only-if-it-is-bytes.patch
BuildArch:      noarch

# The base package is just the CLI, which pulls in the rpmdeplint
# Python modules to do the real work.
Requires:       python3-%{name} = %{version}-%{release}

%description
Rpmdeplint is a tool to find errors in RPM packages in the context of their
dependency graph.


%package -n python3-%{name}
%{?python_provide:%python_provide python3-%{name}}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-pytest
BuildRequires:  python3-six
BuildRequires:  python3-rpm
BuildRequires:  python3-hawkey
BuildRequires:  python3-librepo
Requires:       python3-six
Requires:       python3-rpm
Requires:       python3-hawkey
Requires:       python3-librepo

%description -n python3-%{name}
Rpmdeplint is a tool to find errors in RPM packages in the context of their
dependency graph.

This package provides a Python 3 API for performing the checks.

%prep
%setup -q -n %{name}-%{upstream_version}

%patch0 -p1
%patch1 -p1
%patch2 -p1

rm -rf rpmdeplint.egg-info

%build
%py3_build

%install
%py3_install

%check
py.test-3 rpmdeplint -k "not TestDependencyAnalyzer"
# Acceptance tests do not work in mock because they require .i686 packages.

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%files -n python3-%{name}
%license COPYING
%doc README.rst
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}*.egg-info

%changelog
%autochangelog
