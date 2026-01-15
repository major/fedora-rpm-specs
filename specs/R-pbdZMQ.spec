Name:           R-pbdZMQ
Version:        %R_rpm_version 0.3-14
Release:        %autorelease
Summary:        Programming with Big Data -- Interface to ZeroMQ

License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  zeromq-devel >= 4.0.4

%description
'ZeroMQ' is a well-known library for high-performance asynchronous
messaging in scalable, distributed applications.  This package provides
high level R wrapper functions to easily utilize 'ZeroMQ'. We mainly focus
on interactive client/server programming frameworks.

%prep
%autosetup -c
rm -rf pbdZMQ/inst/zmq_copyright

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
