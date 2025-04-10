# Generated by go2rpm 1.14.0
%bcond check 1
%bcond bootstrap 0

%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# The '-z now' flag, which is the opposite of '-z lazy', isn't supported:
# https://github.com/NVIDIA/go-nvml/issues/18
%global _hardening_ldflags %(echo %_hardening_ldflags | sed 's/-Wl,-z,now//g')

# https://github.com/NVIDIA/go-nvml
%global goipath         github.com/NVIDIA/go-nvml
Version:                0.12.4.1
%global tag             v0.12.4-1

%gometa -L -f

%global common_description %{expand:
Go Bindings for the NVIDIA Management Library (NVML).}

%global golicenses      LICENSE
%global godocs          examples CONTRIBUTING.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Go Bindings for the NVIDIA Management Library (NVML)

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep -A
%autopatch -p1

%if %{without bootstrap}
%generate_buildrequires
%go_generate_buildrequires
%endif

%install
%gopkginstall

%if %{without bootstrap}
%if %{with check}
%check
%gocheck
%endif
%endif

%gopkgfiles

%changelog
%autochangelog
