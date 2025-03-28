# Generated by go2rpm 1.8.2
%bcond_without check

# https://github.com/OliveTin/OliveTin
%global goipath         github.com/OliveTin/OliveTin
Version:                2024.04.14
%global tag             %{version}

%gometa -f
%global goname OliveTin

%global common_description %{expand:
OliveTin gives safe and simple access to predefined shell commands from a web
interface.}

%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md README.md SECURITY.md

Name:           %{goname}
Release:        %autorelease
Summary:        Give safe and simple access to predefined shell commands from a web interface

BuildRequires: systemd-rpm-macros
BuildRequires: googleapis-devel
BuildRequires: protobuf-compiler
BuildRequires: protobuf-devel
BuildRequires: golang-google-grpc
BuildRequires: golang-google-protobuf
BuildRequires: golang-github-grpc-ecosystem-gateway-2
BuildRequires: nodejs20-npm

# Automatically converted from old format: AGPLv3
License:        AGPL-3.0-only
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
sed -i 's/local\///g' %{name}.service

%generate_buildrequires
%go_generate_buildrequires

%build
make protoc
make webui-dist
export LDFLAGS="-X main.version=%{version}%{dist} "
%gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/cmd/%{name}

%install
%gopkginstall
install -m 0755 -vd                             %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/*         %{buildroot}%{_bindir}/

install -m 0644 -vD config.yaml                 %{buildroot}/%{_sysconfdir}/%{name}/config.yaml
install -m 0644 -vD var/manpage/%{name}.1.gz    %{buildroot}%{_mandir}/man1/%{name}.1.gz
install -m 0644 -vD %{name}.service             %{buildroot}/%{_unitdir}/%{name}.service

install -m 0755 -vd                             %{buildroot}/%{_datadir}/%{name}/webui
for d in $(find webui -type d); do
    install --mode 0755 -vd "$d" %{buildroot}%{_datadir}/%{name}/$d
done
for f in $(find webui -type f); do
    install --mode 0644 -vp "$f" %{buildroot}%{_datadir}/%{name}/$f
done

%if %{with check}
%check
%gocheck
%endif

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%doc CODE_OF_CONDUCT.md README.md SECURITY.md
%{_bindir}/%{name}
%config(noreplace) /%{_sysconfdir}/%{name}/config.yaml
%{_datadir}/%{name}/webui
%{_mandir}/man1/%{name}.1.gz
%{_unitdir}/%{name}.service

%gopkgfiles

%changelog
%autochangelog
