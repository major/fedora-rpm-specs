%global with_snapshot 1
%global gitdate 20260723
%global commit 0b3897c9c10d41752e431744c8a5a6502a27828e
%global shortcommit %(c=%{commit}; echo ${c:0:8})
%global desc %{expand: \
qcom-ptool contains various device partitioning utilities like ptool.py,
gen_partitions.py and various sample partition configuration files needed
for Qualcomm SoCs.}

Name:		qcom-ptool
Version:	0.0%{?with_snapshot:^%{gitdate}git%{shortcommit}}
Release:	%autorelease
Summary:	Qualcomm SoC partitioning tool

License:	BSD-3-Clause
URL:		https://github.com/qualcomm-linux/qcom-ptool
%if %{with_snapshot}
Source0:	%{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
%endif

# https://github.com/qualcomm-linux/qcom-ptool/pull/148
Patch0:		148.patch
# https://github.com/qualcomm-linux/qcom-ptool/pull/150
Patch1:		150.patch

BuildArch:	noarch

BuildRequires:	python3-devel

%description
%{desc}

%prep
%if %{with_snapshot}
%autosetup -p1 -n %{name}-%{commit}
%else
%autosetup
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files qcom_ptool

%files -n qcom-ptool -f %{pyproject_files}
%doc README.md CONTRIBUTING.md
%{_bindir}/qcom-ptool

%changelog
%autochangelog
