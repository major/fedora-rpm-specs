# Generated by go2rpm 1.3
%bcond_without check

%global debug_package %{nil}

# https://github.com/iguanesolutions/go-systemd
%global goipath         github.com/iguanesolutions/go-systemd/v5
%global forgeurl        https://github.com/iguanesolutions/go-systemd
Version:                5.1.0

%gometa

%global common_description %{expand:
Golang bindings for systemd notify (including watchdog) & socket activation.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Golang bindings for systemd notify (including watchdog) & socket activation

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/godbus/dbus/v5)
BuildRequires:  golang(github.com/miekg/dns)
BuildRequires:  golang(golang.org/x/net/idna)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
# resolved: need dbus
%gocheck -d resolved
%endif

%gopkgfiles

%changelog
%autochangelog