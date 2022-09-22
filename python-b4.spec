%global srcname b4

%if 0%{?fedora}
%bcond_without attest
%else
# some attestation dependencies not in EPEL
%bcond_with attest
%endif

Name:           python-%{srcname}
Version:        0.8.0
Release:        %autorelease
Summary:        A helper tool to work with public-inbox and patch series
License:        GPLv2
URL:            https://git.kernel.org/pub/scm/utils/%{srcname}/%{srcname}.git
Source0:        https://mirrors.edge.kernel.org/pub/software/devel/%{srcname}/%{srcname}-%{version}.tar.xz
# Unpin version requirements since Fedora 35+'s is newer
Patch0:         b4-unpin-dependencies.patch
%if %{without attest}
Patch1:         b4-no-attest.patch
%endif

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
B4 is a helper utility to work with patches made available via a public-inbox
archive like lore.kernel.org. It is written to make it easier to participate in
a patch-based workflows, like those used in the Linux kernel development.}

%description %{_description}


%package -n %{srcname}
Summary:        %{summary}
Provides:       python%{python3_pkgversion}-%{srcname} = %{version}-%{release}

%description -n %{srcname} %{_description}


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -r requirements.txt


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%pytest


%files -n %{srcname} -f %{pyproject_files}
%license COPYING
%doc README.rst
%{_bindir}/%{srcname}
%{_mandir}/man5/%{srcname}.5.*


%changelog
%autochangelog
