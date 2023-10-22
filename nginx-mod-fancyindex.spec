Name:           nginx-mod-fancyindex
Version:        0.5.2
Release:        %autorelease
Summary:        Nginx FancyIndex module

License:        BSD-2-Clause
URL:            https://github.com/aperezdc/ngx-fancyindex
Source0:        %{url}/releases/download/v%{version}/ngx-fancyindex-%{version}.tar.xz
Source1:        %{url}/releases/download/v%{version}/ngx-fancyindex-%{version}.tar.xz.sig
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/5AA3BC334FD7E3369E7C77B291C559DBE4C9123B

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  nginx-mod-devel
Requires:       nginx

%description
The Fancy Index module makes possible the generation of file listings,
like the built-in autoindex module does, but adding a touch of style.
This is possible because the module allows a certain degree of
customization of the generated content:

* Custom headers. Either local or stored remotely.
* Custom footers. Either local or stored remotely.
* Add you own CSS style rules.
* Allow choosing to sort elements by name (default),
  modification time, or size; both ascending (default),
  or descending.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n ngx-fancyindex-%{version}


%build
%nginx_modconfigure
%nginx_modbuild


%install
pushd %{_vpath_builddir}
install -dm 0755 %{buildroot}%{nginx_moddir}
install -pm 0755 ngx_http_fancyindex_module.so %{buildroot}%{nginx_moddir}
popd

install -dm 0755 %{buildroot}%{nginx_modconfdir}
echo 'load_module "%{nginx_moddir}/ngx_http_fancyindex_module.so";' \
    > %{buildroot}%{nginx_modconfdir}/mod-fancyindex.conf


%files
%license LICENSE
%doc CHANGELOG.md README.rst
%{nginx_moddir}/ngx_http_fancyindex_module.so
%{nginx_modconfdir}/mod-fancyindex.conf

%changelog
%autochangelog
