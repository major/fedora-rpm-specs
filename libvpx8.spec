%global somajor 8
%global sominor 0
%global sotiny  0
%global soversion %{somajor}.%{sominor}.%{sotiny}

Name:			libvpx8
Summary:		Compat package with libvpx libraries
Version:		1.13.1
Release:		1%{?dist}
License:		BSD-3-Clause
URL:			http://www.webmproject.org/code/
Source0:		https://github.com/webmproject/libvpx/archive/v%{version}.tar.gz
Source1:		vpx_config.h
# Thanks to debian.
Source2:		libvpx.ver
# Do not disable FORTIFY_SOURCE=2
Patch0:			libvpx-1.7.0-leave-fortify-source-on.patch
BuildRequires:		gcc
BuildRequires:		gcc-c++
BuildRequires:		make
%ifarch %{ix86} x86_64
BuildRequires:		yasm
%endif
BuildRequires:		doxygen, php-cli, perl(Getopt::Long)

# Explicitly conflict with older libvpx packages that ship libraries
# with the same soname as this compat package
Conflicts: libvpx < 1.14.0

%description
Compatibility package with libvpx libraries ABI version 8.

%prep
%setup -q -n libvpx-%{version}
%patch -P0 -p1 -b .fortify-source-on

%build

%ifarch %{ix86}
%global vpxtarget x86-linux-gcc
%else
%ifarch	x86_64
%global	vpxtarget x86_64-linux-gcc
%else
%ifarch aarch64
%global vpxtarget arm64-linux-gcc
%else
%global vpxtarget generic-gnu
%endif
%endif
%endif

# History: The configure script used to reject the shared flag on the generic target.
# This meant that we needed to fall back to manual shared lib creation.
# However, the modern configure script permits the shared flag and assumes ELF.
# Additionally, the libvpx.ver would need to be updated to work properly.
# As a result, we disable this universally, but keep it around in case we ever need to support
# something "special".
%if "%{vpxtarget}" == "generic-gnu"
%global generic_target 0
%else
%global	generic_target 0
%endif

%set_build_flags

./configure --target=%{vpxtarget} \
--enable-pic --disable-install-srcs \
--enable-vp9-decoder --enable-vp9-encoder \
--enable-experimental \
--enable-vp9-highbitdepth \
--enable-debug \
%if ! %{generic_target}
--enable-shared \
%endif
--enable-install-srcs \
--prefix=%{_prefix} --libdir=%{_libdir} --size-limit=16384x16384

%make_build verbose=true

# Manual shared library creation
# We should never need to do this anymore, and if we do, we need to fix the version-script.
%if %{generic_target}
mkdir tmp
cd tmp
ar x ../libvpx_g.a
cd ..
gcc -fPIC -shared -pthread -lm -Wl,--no-undefined -Wl,-soname,libvpx.so.%{somajor} -Wl,--version-script,%{SOURCE2} -Wl,-z,noexecstack -o libvpx.so.%{soversion} tmp/*.o
rm -rf tmp
%endif

# Temporarily dance the static libs out of the way
# mv libvpx.a libNOTvpx.a
# mv libvpx_g.a libNOTvpx_g.a

# We need to do this so the examples can link against it.
# ln -sf libvpx.so.%{soversion} libvpx.so

# %make_build verbose=true target=examples CONFIG_SHARED=1
# %make_build verbose=true target=docs

# Put them back so the install doesn't fail
# mv libNOTvpx.a libvpx.a
# mv libNOTvpx_g.a libvpx_g.a

%install
make DIST_DIR=%{buildroot}%{_prefix} dist

# Simpler to label the dir as %%doc.
if [ -d %{buildroot}%{_prefix}/docs ]; then
   mv %{buildroot}%{_prefix}/docs doc/
fi

# Again, we should never need to do this anymore.
%if %{generic_target}
install -p libvpx.so.%{soversion} %{buildroot}%{_libdir}
pushd %{buildroot}%{_libdir}
ln -sf libvpx.so.%{soversion} libvpx.so
ln -sf libvpx.so.%{soversion} libvpx.so.%{somajor}
ln -sf libvpx.so.%{soversion} libvpx.so.%{somajor}.%{sominor}
popd
%endif

pushd %{buildroot}
# Stuff we don't need.
rm -rf .%{_prefix}/build/ .%{_prefix}/md5sums.txt .%{_libdir}*/*.a .%{_prefix}/CHANGELOG .%{_prefix}/README
# No, bad google. No treat.
mv .%{_bindir}/examples/* .%{_bindir}
rm -rf .%{_bindir}/examples

# Rename a few examples
mv .%{_bindir}/postproc .%{_bindir}/vp8_postproc
mv .%{_bindir}/simple_decoder .%{_bindir}/vp8_simple_decoder
mv .%{_bindir}/simple_encoder .%{_bindir}/vp8_simple_encoder
mv .%{_bindir}/twopass_encoder .%{_bindir}/vp8_twopass_encoder
# Fix the binary permissions
chmod 755 .%{_bindir}/*
popd

# Get the vpx_config.h file
# Does ppc64le need its own?
%ifarch ppc64 ppc64le
cp -a vpx_config.h %{buildroot}%{_includedir}/vpx/vpx_config-ppc64.h
%else
%ifarch s390 s390x
cp -a vpx_config.h %{buildroot}%{_includedir}/vpx/vpx_config-s390.h
%else
%ifarch %{ix86}
cp -a vpx_config.h %{buildroot}%{_includedir}/vpx/vpx_config-x86.h
%else
cp -a vpx_config.h %{buildroot}%{_includedir}/vpx/vpx_config-%{_arch}.h
%endif
%endif
%endif
cp %{SOURCE1} %{buildroot}%{_includedir}/vpx/vpx_config.h
# for timestamp sync
touch -r AUTHORS %{buildroot}%{_includedir}/vpx/vpx_config.h

mv %{buildroot}%{_prefix}/src/vpx_dsp %{buildroot}%{_includedir}/
mv %{buildroot}%{_prefix}/src/vpx_mem %{buildroot}%{_includedir}/
mv %{buildroot}%{_prefix}/src/vpx_ports %{buildroot}%{_includedir}/
mv %{buildroot}%{_prefix}/src/vpx_scale %{buildroot}%{_includedir}/

rm -rf %{buildroot}%{_prefix}/src

# Remove files that aren't needed for the compat package
rm -rf %{buildroot}%{_bindir}
rm -rf %{buildroot}%{_includedir}
rm -rf %{buildroot}%{_libdir}/*.so
rm -rf %{buildroot}%{_libdir}/pkgconfig/

%files
%license LICENSE
%{_libdir}/libvpx.so.%{somajor}*

%changelog
* Wed Feb 07 2024 Pete Walter <pwalter@fedoraproject.org> - 1.13.1-1
- Initial packaging
