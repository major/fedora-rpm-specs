%global with_snapshot 1
%global gitdate 20261001
%global commit 481caa203fcde01a7c58f16d11ca985656d5cc54
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

BuildArch:	noarch

BuildRequires:	python3-devel
BuildRequires:	python3-pytest

%description
%{desc}

%prep
%if %{with_snapshot}
%autosetup -n %{name}-%{commit}
%else
%autosetup
%endif

%if 0%{?rhel} > 9
# PEP 639 fix
sed -e 's|license = "BSD-3-Clause"|license = {text = "BSD-3-Clause"}|g' -i pyproject.toml
sed -i '/license-files/d' pyproject.toml
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files qcom_ptool

%check
%pytest -v

%files -n qcom-ptool -f %{pyproject_files}
%doc README.md CONTRIBUTING.md
%{_bindir}/qcom-ptool

%changelog
%autochangelog
