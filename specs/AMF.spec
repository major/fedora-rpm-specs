Name:           AMF
Epoch:          1
Version:        1.5.0
Release:        %autorelease
Summary:        Advanced Media Framework (AMF) SDK
License:        MIT
URL:            https://gpuopen.com/advanced-media-framework/
BuildArch:      noarch

# Releases include headers only and we miss documents and samples; so get a
# full tarball without Thirdparty folder.
Source0:        %{name}-cleaned-%{version}.tar.gz
Source1:        %{name}-tarball.sh

%description
A light-weight, portable multimedia framework that abstracts away most of the
platform and API-specific details. %{name} is supported on the closed source AMD
Pro driver and OpenMax on the open source AMD Mesa driver.

%package        devel
Summary:        Development files for %{name}

%description    devel
A light-weight, portable multimedia framework that abstracts away most of the
platform and API-specific details. %{name} is supported on the closed source AMD
Pro driver and OpenMax on the open source AMD Mesa driver.

The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package        samples
Summary:        Sample files for %{name}

%description    samples
The %{name}-samples package contains sample programs and source for applications
that use %{name}.

%package        docs
Summary:        PDF documentation for %{name}

%description    docs
The %{name}-docs package contains the development documentation in PDF format
that is available in the main %{name}-devel package in Markdown format.


%prep
%autosetup -p1

%install
mkdir -p %{buildroot}%{_includedir}/%{name}
cp -fr amf/public/include/* %{buildroot}%{_includedir}/%{name}/

mkdir -p %{buildroot}%{_usrsrc}/%{name}
cp -fr amf/public/* %{buildroot}%{_usrsrc}/%{name}/
rm -fr %{buildroot}%{_usrsrc}/%{name}/include
ln -sf ../../include/AMF %{buildroot}%{_usrsrc}/%{name}/include

# Split out PDF docs
mkdir pdf
mv amf/doc/*pdf pdf/

%files devel
%license LICENSE.txt
%doc amf/doc/*
%{_includedir}/%{name}/

%files samples
%license LICENSE.txt
%{_usrsrc}/%{name}

%files docs
%license LICENSE.txt
%doc pdf/*

%changelog
%autochangelog
