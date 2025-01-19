%global		gitcommit		483f4b3f2d9a125606d47597ae7eff3b38e5bf9d
%global		gitdate		20211016
%global		shortcommit	%(c=%{gitcommit}; echo ${c:0:7})

%global		tarballdate	20211017
%global		tarballtime	1503

%global		base_summary 	User-friendly, customizable image viewer for comic books

%global		base_description \
MComix3 is a user-friendly, customizable image viewer. \
It has been forked from the original MComix project and ported to python3.


Name:			mcomix3
# For now, choose version 0
Version:		0
Release:		0.36.D%{gitdate}git%{shortcommit}%{?dist}
Summary:		%base_summary
# GPL version info is from mcomix/mcomixstarter.py
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:		GPL-2.0-or-later
URL:			https://github.com/multiSnow/mcomix3
# Use git repository directly - with it when modifying source
# we can do it *in git repository* and then we can directly submit
# patch to the upstream by pull request
Source0:		%{name}-%{tarballdate}T%{tarballtime}.tar.bz2
# Source0 is created by Source1
Source1:		create-mcomix3-git-bare-tarball.sh
# Some additional files
Source2:		mcomix3starter.sh.in
# Patches
Patch2:		0002-Change-domain-name-for-gettext.patch
Patch3:		0003-Search-gettext-files-in-system-wide-directory.patch
Patch4:		0004-Workaround-on-zip-archiver-for-contents-info.patch

BuildRequires:	python3-devel
BuildRequires:	%{_bindir}/appstream-util
BuildRequires:	%{_bindir}/desktop-file-install
BuildRequires:	gettext
BuildRequires:	git
BuildArch:		noarch
Requires:		%{name}-base = %{version}-%{release}
Requires:		%{name}-thumbnailer = %{version}-%{release}

Obsoletes:		mcomix < 1.2.2
Obsoletes:		comix < 4.0.5
Provides:		mcomix = 1.2.2


%description
%base_description

%package	base
Summary:	%base_summary
Requires:		gtk3
Requires:		python3-gobject
Requires:		python3-pillow

%description	base
%base_description
This package contains base executable %{name} script.

%package	thumbnailer
Summary:	Thumbnailer for %{name}
Requires:	%{name}-base = %{version}-%{release}

%description	thumbnailer
This package contains thumbnailer for %{name}.

%prep
%setup -q -c -T -a 0

# Setup source git repository
git clone ./%{name}.git
cd %{name}

git config user.name "%{name} Fedora maintainer"
git config user.email "%{name}-owner@fedoraproject.org"
git checkout -b %{version}-%{release}-fedora %{gitcommit}

# Apply patches
cat %{PATCH2} | git am
cat %{PATCH3} | git am
cat %{PATCH4} | git am

%build
pushd %{name}
rm -rf localroot
mkdir localroot

python3 installer.py --srcdir=mcomix --target=$(pwd)/localroot/

# mime
pushd mime
cat mcomix.appdata.xml | \
	sed -e 's|omix|omix3|' | sed -e 's|/mcomix3/|/mcomix/|' \
	> %{name}.appdata.xml
cat mcomix.desktop | sed -e 's|omix|omix3|' > %{name}.desktop
popd

# man
pushd man
cat mcomix.1 | sed -e 's|omix|omix3|' > %{name}.1
popd

popd

# starter script
cat %SOURCE2 | sed -e 's|@python3_sitelib@|%python3_sitelib|g' > mcomix3starter.sh
# create starter script for comicthumb
cat mcomix3starter.sh | sed -e 's|mcomixstarter|comicthumb|' > comicthumbstarter.sh

%install
BUILDTOPDIR=$(pwd)

pushd %{name}
cp -p [A-Z]* ..
popd # from %%name

# Install manually...
SITETOPDIR=%{python3_sitelib}/%{name}
DSTTOPDIR=%{buildroot}${SITETOPDIR}
mkdir -p ${DSTTOPDIR}
mkdir -p ${DSTTOPDIR}/mcomix3
mkdir -p %{buildroot}%{_datadir}/locale
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/

pushd %{name}
rm -rf localroot.2
cp -a localroot localroot.2

pushd localroot.2/mcomix

# Wrapper script
install -cpm 0755 ${BUILDTOPDIR}/mcomix3starter.sh ${DSTTOPDIR}
install -cpm 0755 ${BUILDTOPDIR}/comicthumbstarter.sh ${DSTTOPDIR}
# locale files
find mcomix/messages/* -type f | while read f
do
	dir=$(dirname $f)
	mv $f $dir/%{name}.mo
done
mv mcomix/messages/* %{buildroot}%{_datadir}/locale/

# duplicate icon
for dir in mcomix/images/*x*/
do
	basedir=$(basename $dir)
	mkdir -p %{buildroot}%{_datadir}/icons/hicolor/$basedir/apps
	cp -p $dir/*png %{buildroot}%{_datadir}/icons/hicolor/$basedir/apps/%{name}.png
done

# scripts
mv comicthumb.py ${DSTTOPDIR}/
mv mcomixstarter.py ${DSTTOPDIR}/

# data files
mv mcomix/ ${DSTTOPDIR}/mcomix3/

# Ensure that all files are installed
popd # from localroot.2/mcomix
rmdir localroot.2/mcomix
rmdir localroot.2

popd # from %%name
# Wrapper symlink
mkdir %{buildroot}/%{_bindir}
ln -sf ../../${SITETOPDIR}/mcomix3starter.sh %{buildroot}%{_bindir}/mcomix3
ln -sf ../../${SITETOPDIR}/comicthumbstarter.sh %{buildroot}%{_bindir}/comicthumb

pushd %{name}
# mime data
pushd mime
install -D -cpm 0644 comicthumb.thumbnailer %{buildroot}%{_datadir}/thumbnailers/comicthumb.thumbnailer
install -D -cpm 0644 %{name}.appdata.xml  %{buildroot}%{_metainfodir}/%{name}.appdata.xml

## desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
	--remove-category Application \
	--dir %{buildroot}%{_datadir}/applications/ \
	./%{name}.desktop

## Not installing mimetype icon files for now
popd # from mime

# man
pushd man
mkdir -p %{buildroot}%{_mandir}/man1
install -cpm 0644 \
	comicthumb.1 \
	%{name}.1 \
	%{buildroot}%{_mandir}/man1/
popd # from man

popd # from %%name

%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml
# TODO: support ./test/run.py

%files

%files	base -f %{name}.lang
%license	COPYING
%doc		ChangeLog
%doc		README*
%doc		TODO

%{_bindir}/%{name}

%{python3_sitelib}/%{name}/

# Do not own %%{_datadir}/icons/hicolor explicitly
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop

%{_mandir}/man1/%{name}.1*

%files	thumbnailer
%{_bindir}/comicthumb
%{_datadir}/thumbnailers/comicthumb.thumbnailer
%{_mandir}/man1/comicthumb.1*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.36.D20211016git483f4b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Aug 17 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0-0.35.D20211016git483f4b3
- Workaround for zip archiver for contents info

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0-0.34.D20211016git483f4b3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.33.D20211016git483f4b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0-0.32.D20211016git483f4b3
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.31.D20211016git483f4b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.30.D20211016git483f4b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.29.D20211016git483f4b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0-0.28.D20211016git483f4b3
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.27.D20211016git483f4b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.26.D20211016git483f4b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0-0.25.D20211016git483f4b3
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.24.D20211016git483f4b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 10 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0-0.23.D20211016git483f4b3
- Fix up startup wrapper script wrt positional parameters (bug 2021355)

* Sun Oct 17 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0-0.22.D20211016git483f4b3
- Update to the latest git

* Thu Sep 23 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0-0.21.D20210916gitcff5fc3
- Update to the latest git

* Sun Sep 12 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0-0.20.D20210829git8cd3ebe
- Update to the latest git
- Split whole package into -base and -thumbnailer (ref: bug 1965831)

* Tue Aug 10 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0-0.19.D20210803gitd003e64
- Update to the latest git

* Fri Jul 30 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0-0.18.D20210526git9eb4fc7
- Update to the latest git

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.D20210507gitaf858a6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0-0.16.D20210507gitaf858a6
- Rebuilt for Python 3.10

* Fri May  7 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0-0.15.D20210507gitaf858a6
- Update to the latest git

* Sat May  1 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0-0.14.D20210423git139344e
- Update to the latest git

* Thu Apr  1 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0-0.13.D20210329git523f08f
- Update to the latest git

* Sun Mar 28 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0-0.12.D20210321gitdfe9520
- Apply bug 1941827 suggestion

* Fri Mar 26 2021 Mamoru TASAKA <mtasaka@fedoraproject.org>
- Update to the latest git (20210321gitdfe9520)

* Tue Mar 23 2021 Mikhail Novosyolov <m.novosyolov@rosalinux.ru>
- Simply mcomix3 starter script (bug 1941827)
- Also create starter script for comicthumb (bug 1941827)

* Tue Mar  9 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0-0.11.D20210226gite5f39a2
- Update to the latest git

* Tue Mar  9 2021 Mamoru TASAKA <mtasaka@fedoraproject.org>
- Install mime related files and comicthumb

* Mon Feb 22 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0-0.10.D20201223git9ba2f5b
- Update to the latest git

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.D20191205gita098f81
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.D20191205gita098f81
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0-0.7.D20191205gita098f81
- Rebuilt for Python 3.9

* Fri May  8 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> 0-0.6.D20191205gita098f81
- Pass argument to start script (Patch by Sean Morgan <sean@shellytrail.net>)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.D20191205gita098f81
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 30 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> 0-0.4.D20191205gita098f81
- Update to latest git (20191205)

* Fri Nov  8 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> 0-0.2.D20190616git0405a23
- Reflect package review suggestions (bug 1768447)

* Mon Nov 04 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> 0-0.1.D20190616git0405a23
- Initial packaging
