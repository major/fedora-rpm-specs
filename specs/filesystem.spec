%bcond merged_sbin 1

Summary: The basic directory layout for a Linux system
Name: filesystem
Version: 3.18
Release: %autorelease
License: LicenseRef-Fedora-Public-Domain
URL: https://pagure.io/filesystem
Source1: https://pagure.io/filesystem/raw/master/f/lang-exceptions
Source2: iso_639.sed
Source3: iso_3166.sed
Source4: sbin-filenames
Source5: filesystem.attr
Source6: filesystem.req
Source7: macros.filesystem
BuildRequires: iso-codes
Requires(pre): setup

Provides:   filesystem-afs = %{version}-%{release}
Obsoletes:  filesystem-afs <= 3.14-2

%if %{with merged_sbin}
# A virtual provides to indicate merged bin and sbin directories.
# This is intended in particular for rpm-ostree, so it can conditionalize
# how it sets up the initial directory structure.
Provides:   filesystem(merged-sbin) = 1

# A virtual provides that packages can use to make sure that the
# symlinks from /usr/sbin/foo to /usr/bin/foo will be automatically
# created (if /usr/sbin is not a symlink itself).
Provides:   filesystem(unmerged-sbin-symlinks) = 1
%endif

# This is needed for rpm-4.20
%global debug_package %{nil}

%description
The filesystem package is one of the basic packages that is installed
on a Linux system. Filesystem contains the basic directory layout
for a Linux operating system, including the correct permissions for
the directories.

%package content
Summary: Directory ownership content of the filesystem package

%description content
This subpackage of filesystem package contains just the file with
the directories owned by the filesystem package. This can be used
during the build process instead of calling rpm -ql filesystem.

%package srpm-macros
Summary: Macros for the sbin-merge
BuildArch: noarch

%description srpm-macros
This subpackage of filesystem package contains rpm macro definitions
and an rpm attribute generator.

%prep
rm -f $RPM_BUILD_DIR/filelist

%build

%install
rm -rf %{buildroot}
mkdir %{buildroot}
install -p -c -m755 %SOURCE2 %{buildroot}/iso_639.sed
install -p -c -m755 %SOURCE3 %{buildroot}/iso_3166.sed

cd %{buildroot}

Paths=(
        afs boot dev \
        etc/{X11/{applnk,fontpath.d,xinit/{xinitrc,xinput}.d},xdg/autostart,opt,pm/{config.d,power.d,sleep.d},skel,sysconfig,keys/ima,pki,bash_completion.d,default,rwtab.d,statetab.d} \
        home media mnt opt root run srv tmp \
        usr/{bin,games,include,%{_lib}/{bpf,games,X11,pm-utils/{module.d,power.d,sleep.d}},lib/{debug/{.dwz,usr},games,locale,modules,sysimage,systemd/{system,user},sysusers.d,tmpfiles.d},libexec,local/{bin,etc,games,lib,%{_lib}/bpf,src,share/{applications,man/man{1,2,3,4,5,6,7,8,9,n,1x,2x,3x,4x,5x,6x,7x,8x,9x},info},libexec,include,},share/{aclocal,appdata,applications,augeas/lenses,backgrounds,bash-completion{,/completions,/helpers},desktop-directories,dict,doc,empty,fish/vendor_completions.d,games,gnome,help,icons,idl,info,licenses,man/man{1,2,3,4,5,6,7,8,9,n,1x,2x,3x,4x,5x,6x,7x,8x,9x,0p,1p,3p},metainfo,mime-info,misc,modulefiles,omf,pixmaps,sounds,themes,xsessions,X11/fonts,wayland-sessions,zsh/site-functions},src,src/kernels,src/debug} \
        var/{adm,empty,ftp,lib/{games,misc,rpm-state},local,log,nis,preserve,spool/{mail,lpd},tmp,db,cache/bpf,opt,games,yp}
)
for i in "${Paths[@]}"; do
    mkdir -p "$i"
done

ln -snf ../var/tmp usr/tmp
ln -snf spool/mail var/mail
ln -snf usr/bin bin
ln -snf usr/sbin sbin
ln -snf usr/lib lib
ln -snf usr/%{_lib} %{_lib}
ln -snf ../run var/run
ln -snf ../run/lock var/lock
ln -snf usr/bin usr/lib/debug/bin
ln -snf usr/lib usr/lib/debug/lib
ln -snf usr/%{_lib} usr/lib/debug/%{_lib}
ln -snf ../.dwz usr/lib/debug/usr/.dwz
ln -snf usr/sbin usr/lib/debug/sbin

%if %{with merged_sbin}
ln -snf bin usr/sbin
ln -snf bin usr/local/sbin
%else
mkdir -p usr/sbin
mkdir -p usr/local/sbin
%endif

sed -n -f %{buildroot}/iso_639.sed /usr/share/xml/iso-codes/iso_639.xml \
  >%{buildroot}/iso_639.tab
sed -n -f %{buildroot}/iso_3166.sed /usr/share/xml/iso-codes/iso_3166.xml \
  >%{buildroot}/iso_3166.tab

grep -v "^$" %{buildroot}/iso_639.tab | grep -v "^#" | while read a b c d ; do
    [[ "$d" =~ "^Reserved" ]] && continue
    [[ "$d" =~ "^No linguistic" ]] && continue

    locale=$c
    if [ "$locale" = "XX" ]; then
        locale=$b
    fi
    echo "%lang(${locale})	/usr/share/locale/${locale}" >> $RPM_BUILD_DIR/filelist
    echo "%lang(${locale}) %ghost %config(missingok) /usr/share/man/${locale}" >>$RPM_BUILD_DIR/filelist
done
cat %{SOURCE1} | grep -v "^#" | grep -v "^$" | while read loc ; do
    locale=$loc
    locality=
    special=
    [[ "$locale" =~ "@" ]] && locale=${locale%%%%@*}
    [[ "$locale" =~ "_" ]] && locality=${locale##*_}
    [[ "$locality" =~ "." ]] && locality=${locality%%%%.*}
    [[ "$loc" =~ "_" ]] || [[ "$loc" =~ "@" ]] || special=$loc

    # If the locality is not official, skip it
    if [ -n "$locality" ]; then
        grep -q "^$locality" %{buildroot}/iso_3166.tab || continue
    fi
    # If the locale is not official and not special, skip it
    if [ -z "$special" ]; then
        egrep -q "[[:space:]]${locale%%_*}[[:space:]]" \
           %{buildroot}/iso_639.tab || continue
    fi
    echo "%lang(${locale})	/usr/share/locale/${loc}" >> $RPM_BUILD_DIR/filelist
    echo "%lang(${locale})  %ghost %config(missingok) /usr/share/man/${loc}" >> $RPM_BUILD_DIR/filelist
done

rm -f %{buildroot}/iso_639.tab
rm -f %{buildroot}/iso_639.sed
rm -f %{buildroot}/iso_3166.tab
rm -f %{buildroot}/iso_3166.sed

cat $RPM_BUILD_DIR/filelist | grep "locale" | while read a b ; do
    mkdir -p -m 755 %{buildroot}/$b/LC_MESSAGES
done

cat $RPM_BUILD_DIR/filelist | grep "/share/man" | while read a b c d; do
    mkdir -p -m 755 %{buildroot}/$d/man{1,2,3,4,5,6,7,8,9,n,1x,2x,3x,4x,5x,6x,7x,8x,9x,0p,1p,3p}
done

for i in man{1,2,3,4,5,6,7,8,9,n,1x,2x,3x,4x,5x,6x,7x,8x,9x,0p,1p,3p}; do
   echo "/usr/share/man/$i" >>$RPM_BUILD_DIR/filelist
done

mkdir -p %{buildroot}%{_datadir}/filesystem
#find all dirs in the buildroot owned by filesystem and store them
find %{buildroot} -mindepth 0 | sed -e 's|%{buildroot}|/|' -e 's|//|/|' \
 | LC_ALL=C sort | grep -v filesystem >%{buildroot}%{_datadir}/filesystem/paths

cp -p %{SOURCE4} %{buildroot}%{_datadir}/filesystem/sbin-filenames

mkdir -p %{buildroot}%{_fileattrsdir} %{buildroot}%{_rpmconfigdir} %{buildroot}%{rpmmacrodir}
cp -p %{SOURCE5} %{buildroot}%{_fileattrsdir}/filesystem.attr
cp -p %{SOURCE6} %{buildroot}%{_rpmconfigdir}/filesystem.req
cp -p %{SOURCE7} %{buildroot}%{rpmmacrodir}/macros.filesystem

%pretrans -p <lua>
--# If we are running in pretrans in a fresh root, there is no /usr and
--# symlinks. We cannot be sure, to be the very first rpm in the
--# transaction list. Let's create the needed base directories and symlinks
--# here, to place the files from other packages in the right locations.
--# When our rpm is unpacked by cpio, it will set all permissions and modes
--# later.
posix.mkdir("/usr")
posix.mkdir("/usr/bin")
posix.mkdir("/usr/lib")
posix.mkdir("/usr/lib/debug")
posix.mkdir("/usr/lib/debug/usr/")
posix.mkdir("/usr/lib/debug/usr/bin")
posix.mkdir("/usr/lib/debug/usr/lib")
posix.mkdir("/usr/lib/debug/usr/%{_lib}")
posix.mkdir("/usr/%{_lib}")
posix.symlink("usr/bin", "/bin")
posix.symlink("usr/sbin", "/sbin")
posix.symlink("usr/lib", "/lib")
posix.symlink("usr/bin", "/usr/lib/debug/bin")
posix.symlink("usr/lib", "/usr/lib/debug/lib")
posix.symlink("usr/%{_lib}", "/usr/lib/debug/%{_lib}")
posix.symlink("../.dwz", "/usr/lib/debug/usr/.dwz")
posix.symlink("usr/sbin", "/usr/lib/debug/sbin")
posix.symlink("usr/%{_lib}", "/%{_lib}")
posix.mkdir("/run")
posix.mkdir("/proc")
posix.mkdir("/sys")
posix.chmod("/proc", 0555)
posix.chmod("/sys", 0555)
st = posix.stat("/media")
if st and st.type == "link" then
  os.remove("/media")
end
posix.mkdir("/var")
posix.symlink("../run", "/var/run")
posix.symlink("../run/lock", "/var/lock")

%if %{with merged_sbin}
posix.symlink("bin", "/usr/sbin")
posix.symlink("bin", "/usr/lib/debug/usr/sbin")
posix.symlink("bin", "/usr/local/sbin")
%else
posix.mkdir("/usr/sbin")
posix.mkdir("/usr/lib/debug/usr/sbin")
%endif

%if %{with merged_sbin}
%global sbin_filenames %{lua:
print('{\\n')
io.input(sources[4])
for v in io.lines() do
  print('  ["'..v..'"] = true,\\n')
end
print('}')
}

%filetriggerin -p <lua> -- /usr/bin
--# This implements filesystem(unmerged-sbin-symlinks) feature.
st = posix.stat("/usr/sbin")
if not st or st.type == "link" then
  return
end

filenames = %sbin_filenames

a = rpm.next_file()
while a do
    name = a:match("^.+/(.+)$")
    if filenames[name] then
      b = "/usr/sbin/"..name
      sta = posix.stat(a)
      stb = posix.stat(b)

      if sta and not stb then
        print('Symlinking /usr/sbin/'..name..'->/usr/bin/'..name)
        posix.symlink("../bin/"..name, "/usr/sbin/"..name)
      end
    end

    a = rpm.next_file()
end

%filetriggerpostun -p <lua> -- /usr/bin
--# This implements filesystem(unmerged-sbin-symlinks) feature.
st = posix.stat("/usr/sbin")
if not st or st.type == "link" then
  return
end

filenames = %sbin_filenames

a = rpm.next_file()
while a do
    name = a:match("^.+/(.+)$")
    if filenames[name] then
      b = "/usr/sbin/"..name
      sta = posix.stat(a)
      stb = posix.stat(b)

      if sta and not stb then
        print('Symlinking '..b..'->/usr/bin/'..name)
        posix.symlink("../bin/"..name, b)
      elseif not sta and stb and stb.type == "link" then
        target = posix.readlink(b)
        if target ==  "../bin/"..name then
          print('Removing', b)
          os.remove(b)
        else
          print('Not touching '..b..' -> '..target)
        end
      end
    end

    a = rpm.next_file()
end

%filetriggerpostun -p <lua> -- /sbin /usr/sbin
--# This implements filesystem(unmerged-sbin-symlinks) feature.
st = posix.stat("/usr/sbin")
if not st or st.type == "link" then
  return
end

filenames = %sbin_filenames

b = rpm.next_file()
while b do
    name = b:match("^.+/(.+)$")

    if filenames[name] then
      a = "/usr/bin/"..name
      sta = posix.stat(a)
      stb = posix.stat(b)

      if sta and not stb then
        print('Symlinking /usr/sbin/'..name..'->'..a)
        posix.symlink("../bin/"..name, "/usr/sbin/"..name)
      end
    end

    b = rpm.next_file()
end

%global merge_scriptlet %{expand:
--# Symlink /usr/sbin→/usr/bin and /usr/local/sbin→/usr/local/bin if possible

for _,path in pairs({"/usr/sbin", "/usr/local/sbin"}) do
  st = posix.stat(path)
  if st and st.type ~= "link" then
    good = true

    items = rpm.glob(path.."/*")
    for _,v in pairs(items) do
      --# rpm.glob() returns the original pattern if match fails :(((
      if v ~= path.."/*" then
        st = posix.stat(v)

        if not st then
          print("Could not stat "..v)
        else
          if st.type ~= "link" then
            print("/usr/sbin cannot be merged, found "..v)
            good = false
            break
          end

          target = posix.readlink(v)
          name = v:match("^.+/(.+)$")
          if target ~= "../bin/"..name then
            print("/usr/sbin cannot be merged, "..v.." points to "..target)
            good = false
            break
          end
        end
      end
    end

    if good then
      print("All files under "..path.." are symlinks; linking to ./bin...")

      for _,v in pairs(items) do
        os.remove(v)
      end
      os.remove(path)
      posix.symlink("bin", path)
      print("...done")
    end
  end
end
}
%endif

%posttrans -p <lua>
--# we need to restorecon on some dirs created in %pretrans or by other packages
if posix.access ("/usr/sbin/restorecon", "x") then
  rpm.execute("/usr/sbin/restorecon", "/var", "/var/run", "/var/lock", "/sys", "/boot", "/dev", "/media", "/afs")
  rpm.execute("/usr/sbin/restorecon", "-r", "/usr/lib/debug")
end

%if %{with merged_sbin}
%merge_scriptlet

%transfiletriggerpostun -p <lua> -- /sbin /usr/sbin
%merge_scriptlet
%endif

%files content
%dir %{_datadir}/filesystem
%{_datadir}/filesystem/paths

%files srpm-macros
%{_datadir}/filesystem/sbin-filenames
%{_fileattrsdir}/filesystem.attr
%{_rpmconfigdir}/filesystem.req
%{rpmmacrodir}/macros.filesystem

%files -f filelist
%defattr(0755,root,root,0755)
%dir %attr(555,root,root) /
/bin
/sbin
%attr(555,root,root) /boot
%attr(555,root,root) /afs
/dev
%dir /etc
/etc/X11
/etc/xdg
/etc/opt
/etc/pm
/etc/skel
/etc/sysconfig
/etc/keys
/etc/pki
/etc/bash_completion.d/
%dir /etc/default
%dir /etc/rwtab.d
%dir /etc/statetab.d
/home
/lib
%ifarch x86_64 ppc64 sparc64 s390x aarch64 ppc64le mips64 mips64el riscv64
/%{_lib}
%endif
/media
%dir /mnt
%dir /opt
%ghost %attr(555,root,root) /proc
%attr(550,root,root) /root
/run
/srv
%ghost %attr(555,root,root) /sys
%attr(1777,root,root) /tmp
%dir /usr
%attr(555,root,root) /usr/bin
%if %{with merged_sbin}
%ghost /usr/sbin
%else
%attr(555,root,root) /usr/sbin
%endif
/usr/games
/usr/include
%dir %attr(555,root,root) /usr/lib
%dir /usr/lib/sysimage
%dir /usr/lib/systemd
/usr/lib/systemd/system
/usr/lib/systemd/user
%dir /usr/lib/sysusers.d
%dir /usr/lib/tmpfiles.d
%dir /usr/lib/locale
%dir /usr/lib/modules
%dir /usr/lib/debug
%dir /usr/lib/debug/.dwz
%ghost /usr/lib/debug/bin
%ghost /usr/lib/debug/lib
%ghost /usr/lib/debug/%{_lib}
%ghost %dir /usr/lib/debug/usr
%ghost /usr/lib/debug/usr/bin
%ghost /usr/lib/debug/usr/sbin
%ghost /usr/lib/debug/usr/lib
%ghost /usr/lib/debug/usr/%{_lib}
%ghost /usr/lib/debug/usr/.dwz
%ghost /usr/lib/debug/sbin
%attr(555,root,root) /usr/lib/games
%ifarch x86_64 ppc64 sparc64 s390x aarch64 ppc64le mips64 mips64el riscv64
%attr(555,root,root) /usr/%{_lib}
%else
%attr(555,root,root) /usr/lib/bpf
%attr(555,root,root) /usr/lib/X11
%attr(555,root,root) /usr/lib/pm-utils
%endif
/usr/libexec
%dir /usr/local
%if %{with merged_sbin}
%ghost /usr/local/sbin
%else
/usr/local/sbin
%endif
/usr/local/etc
/usr/local/bin
/usr/local/games
/usr/local/include
/usr/local/lib*
/usr/local/share
/usr/local/src
%dir /usr/share
/usr/share/aclocal
/usr/share/appdata
/usr/share/applications
/usr/share/augeas
/usr/share/backgrounds
%dir /usr/share/bash-completion
/usr/share/bash-completion/completions
/usr/share/bash-completion/helpers
/usr/share/desktop-directories
/usr/share/dict
/usr/share/doc
%attr(555,root,root) %dir /usr/share/empty
/usr/share/fish
/usr/share/games
/usr/share/gnome
/usr/share/help
/usr/share/icons
/usr/share/idl
/usr/share/info
%dir /usr/share/licenses
%dir /usr/share/locale
%dir /usr/share/man
/usr/share/metainfo
/usr/share/mime-info
/usr/share/misc
%dir /usr/share/modulefiles
/usr/share/omf
/usr/share/pixmaps
/usr/share/sounds
/usr/share/themes
/usr/share/xsessions
%dir /usr/share/X11
/usr/share/X11/fonts
/usr/share/wayland-sessions
/usr/share/zsh
/usr/src
/usr/tmp
%dir /var
/var/adm
%dir /var/cache
/var/cache/bpf
/var/db
/var/empty
/var/ftp
/var/games
/var/lib
/var/local
%ghost /var/lock
/var/log
/var/mail
/var/nis
/var/opt
/var/preserve
%ghost /var/run
%dir /var/spool
%attr(755,root,root) /var/spool/lpd
%attr(775,root,mail) /var/spool/mail
%attr(1777,root,root) /var/tmp
/var/yp

%changelog
%autochangelog
