# Generated by go2rpm 1.9.0
%bcond_without check

# https://github.com/nats-io/nats-streaming-server
%global goipath         github.com/nats-io/nats-streaming-server
Version:                0.25.6

%gometa -f


%global common_description %{expand:
NATS Streaming is an extremely performant, lightweight reliable
streaming platform built on NATS}

%global golicenses      LICENSE
%global godocs          CODE-OF-CONDUCT.md GOVERNANCE.md MAINTAINERS.md\\\
                        README.md TODO.md

Name:           %{goname}
Release:        %autorelease
Summary:        NATS Streaming System Server

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/nats-streaming-server %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
# logger, stores: need network
%gocheck -d server -d logger -d stores
%endif

%files
%license LICENSE
%doc CODE-OF-CONDUCT.md GOVERNANCE.md MAINTAINERS.md README.md TODO.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog