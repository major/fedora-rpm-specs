%bcond_without check

# gitlab.com/esr/gif2png
%global goipath         gitlab.com/esr/gif2png
%global forgeurl        https://gitlab.com/esr/gif2png
Version:                3.0.4
%global tag             3.0.4

%gometa -L -f

Summary:        A GIF to PNG converter
Name:           gif2png
Release:        %autorelease
License:        BSD-2-Clause AND BSD-3-Clause
URL:            http://www.catb.org/~esr/gif2png/
Source0:        %{url}%{name}-%{version}.tar.gz
Source1:        vendor.tar.bz2
Source2:        go-vendor-tools.toml

BuildRequires:  go-vendor-tools
BuildRequires:  compiler(go-compiler)
BuildRequires:  make
BuildRequires:  diffutils

%description
The gif2png program converts files from the Graphic Interchange Format (GIF) to
Portable Network Graphics (PNG).

%prep
%goprep -p1
tar -xf %{S:1}

%generate_buildrequires
%go_vendor_license_buildrequires -c %{S:2}

%build
%global gomodulesmode GO111MODULE=on
%gobuild -mod=vendor -o %{gobuilddir}/bin/gif2png %{goipath}

%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/gif2png %{buildroot}%{_bindir}/gif2png
ln -sf gif2png                          %{buildroot}%{_bindir}/webpng

install -m 0755 -vd                     %{buildroot}%{_mandir}/man1
install -m 0644 -vp gif2png.1           %{buildroot}%{_mandir}/man1/gif2png.1
ln -sf gif2png.1                        %{buildroot}%{_mandir}/man1/webpng.1

%check
%go_vendor_license_check -c %{S:2}
%if %{with check}
cp %{gobuilddir}/bin/gif2png .
%make_build -C tests gif2png-test
%endif

%files -f %{go_vendor_license_filelist}
%doc README.adoc NEWS.adoc
%{_bindir}/gif2png
%{_bindir}/webpng
%{_mandir}/man1/gif2png.1*
%{_mandir}/man1/webpng.1*

%changelog
%autochangelog
