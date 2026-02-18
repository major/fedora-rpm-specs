%global realname corba
# Technically, we're almost noarch (ic has some binary-specific files); but
# erlang whose directories we install into is not.
%global debug_package %{nil}


%ifarch %{arm} %{mips} riscv64 %{ix86}
# MIPS and RISC-V does not have all dependencies for fop yet.
# For some reason, fop hangs on arm, so for now don't generate docs by
# default.
%bcond_with doc
%else
%bcond_without doc
%endif


Name:		erlang-%{realname}
Version:	5.2.2
Epoch:		1
Release:	%autorelease
Summary:	Erlang CORBA libraries
License:	Apache-2.0
URL:		https://github.com/erlang/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch:		erlang-corba-0001-Add-files-from-OTP-tree.patch
Patch:		erlang-corba-0002-Edit-OTP-files-to-allow-out-of-tree-build.patch
Patch:		erlang-corba-0003-Do-not-install-C-sources.patch
Patch:		erlang-corba-0004-Do-not-install-Java-sources.patch
Patch:		erlang-corba-0005-Do-not-install-erlang-sources.patch
Patch:		erlang-corba-0006-Do-not-install-examples.patch
Patch:		erlang-corba-0007-Fix-javadoc.patch
BuildRequires:	erlang-erl_docgen
BuildRequires:	erlang-erl_interface
BuildRequires:	erlang-erts
BuildRequires:	erlang-ftp
BuildRequires:	erlang-jinterface
BuildRequires:	erlang-parsetools
BuildRequires:	erlang-rpm-macros
BuildRequires:	gcc
BuildRequires:	java-25-devel
%if %{with doc}
BuildRequires:	fop
BuildRequires:	libxslt
%endif
BuildRequires: make
# FIXME no autodetect yet
#BuildRequires:	erlang-cosEvent
#BuildRequires:	erlang-cosNotification
#BuildRequires:	erlang-cosProperty
#BuildRequires:	erlang-cosTime
#BuildRequires:	erlang-orber
ExclusiveArch:	%{java_arches}


%description
A set of Erlang applications, that implements a CORBA compliant Object Request
Broker (ORB) and a number of Object Managemnt Group (OMG) standard services.

%if %{with doc}
%package doc
Summary: Erlang CORBA documentation
BuildArch: noarch

%description doc
Documentation for Erlang.
%endif

%package -n erlang-cosEvent
Summary: Orber OMG Event Service
Requires: erlang-orber%{?_isa}

%description -n erlang-cosEvent
Orber OMG Event Service.

%package -n erlang-cosEventDomain
Summary: Orber OMG Event Domain Service
Requires: erlang-cosNotification%{?_isa}
Requires: erlang-orber%{?_isa}

%description -n erlang-cosEventDomain
Orber OMG Event Domain Service.

%package -n erlang-cosFileTransfer
Summary: Orber OMG File Transfer Service
Requires: erlang-cosProperty%{?_isa}
Requires: erlang-orber%{?_isa}

%description -n erlang-cosFileTransfer
Orber OMG File Transfer Service.

%package -n erlang-cosNotification
Summary: Orber OMG Notification Service
Requires: erlang-cosEvent%{?_isa}
Requires: erlang-cosTime%{?_isa}
Requires: erlang-orber%{?_isa}

%description -n erlang-cosNotification
Orber OMG Notification Service.

%package -n erlang-cosProperty
Summary: Orber OMG Property Service
Requires: erlang-orber%{?_isa}

%description -n erlang-cosProperty
Orber OMG Property Service.

%package -n erlang-cosTime
Summary: Orber OMG Timer and TimerEvent Service
Requires: erlang-cosEvent%{?_isa}
Requires: erlang-orber%{?_isa}

%description -n erlang-cosTime
Orber OMG Timer and TimerEvent Service.

%package -n erlang-cosTransactions
Summary: Orber OMG Transaction Service
Requires: erlang-orber%{?_isa}

%description -n erlang-cosTransactions
Orber OMG Transaction Service.

%package -n erlang-ic
Summary: IDL compiler
Requires: erlang-jinterface
Requires: javapackages-tools

%description -n erlang-ic
IDL compiler.

%package -n erlang-orber
Summary: A CORBA Object Request Broker

%description -n erlang-orber
A CORBA Object Request Broker.


%prep
%autosetup -p1 -n %{realname}-%{version}


%build
CFLAGS="$RPM_OPT_FLAGS" ERL_TOP=`pwd` make %{?_smp_mflags} V=1
%if %{with doc}
CFLAGS="$RPM_OPT_FLAGS" ERL_TOP=`pwd` make docs V=1
%endif


%install
ERL_TOP=`pwd` make install DESTDIR=%{buildroot}%{_erldir}
%if %{with doc}
ERL_TOP=`pwd` make install-docs DESTDIR=%{buildroot}%{_erldir}
%endif

# erlang-ic
install -m 0755 -d "%{buildroot}%{_javadir}/erlang"
ic_lib_dir="$(ls -d1 %{buildroot}%{_libdir}/erlang/lib/ic-*/ | sed "s,^%{buildroot},,")"
test -d "%{buildroot}$ic_lib_dir"
ln -s "${ic_lib_dir}priv/ic.jar" "%{buildroot}%{_javadir}/erlang/"

%if %{with doc}
# Move man-pages to a system-wide directory - in the same way as Debian did
# Erlang files from man 3 have too generic names
for manpage in %{buildroot}%{_libdir}/erlang/man/man3/*
do
	mv ${manpage} ${manpage}erl
done
mkdir -p %{buildroot}%{_mandir}/
mv %{buildroot}%{_libdir}/erlang/man/* %{buildroot}%{_mandir}/
%endif

# Relocate doc-files into the proper directory
%if %{with doc}
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}/lib
pushd .
cd %{buildroot}%{_libdir}/erlang
mv -v doc %{buildroot}%{_docdir}/%{name}-%{version}
cd %{buildroot}%{_libdir}/erlang/lib
for i in * ; do mv -v $i/doc %{buildroot}%{_docdir}/%{name}-%{version}/lib/$i || true ; done
popd
for i in ic orber ; do mv -v lib/$i/examples %{buildroot}%{_docdir}/%{name}-%{version}/lib/$i-%{version}/examples || true ; done
cp -av AUTHORS CONTRIBUTING.md README.md %{buildroot}%{_docdir}/%{name}-%{version}
# We'll package it by marking it explicitly as doc - see below
rm -f %{buildroot}%{_libdir}/erlang/README.md %{buildroot}%{_libdir}/erlang/COPYRIGHT
%endif

# Do not install info files - they are almost empty and useless
find %{buildroot}%{_libdir}/erlang -type f -name info -exec rm -f {} \;


%if %{with doc}
%files doc
%dir %{_docdir}/%{name}-%{version}/
%doc %{_docdir}/%{name}-%{version}/AUTHORS
%doc %{_docdir}/%{name}-%{version}/CONTRIBUTING.md
%doc %{_docdir}/%{name}-%{version}/README.md
%doc %{_docdir}/%{name}-%{version}/doc
%doc %{_docdir}/%{name}-%{version}/lib/
%license COPYRIGHT
%license LICENSE.txt
%endif

%files -n erlang-cosEvent
%license COPYRIGHT
%license LICENSE.txt
%{_libdir}/erlang/lib/cosEvent-*/
%if %{with doc}
%{_mandir}/man3/cosEventApp.*
%{_mandir}/man3/CosEventChannelAdmin.*
%{_mandir}/man3/CosEventChannelAdmin_ConsumerAdmin.*
%{_mandir}/man3/CosEventChannelAdmin_EventChannel.*
%{_mandir}/man3/CosEventChannelAdmin_ProxyPullConsumer.*
%{_mandir}/man3/CosEventChannelAdmin_ProxyPullSupplier.*
%{_mandir}/man3/CosEventChannelAdmin_ProxyPushConsumer.*
%{_mandir}/man3/CosEventChannelAdmin_ProxyPushSupplier.*
%{_mandir}/man3/CosEventChannelAdmin_SupplierAdmin.*
%endif

%files -n erlang-cosEventDomain
%license COPYRIGHT
%license LICENSE.txt
%{_libdir}/erlang/lib/cosEventDomain-*/
%if %{with doc}
%{_mandir}/man3/CosEventDomainAdmin.*
%{_mandir}/man3/CosEventDomainAdmin_EventDomain.*
%{_mandir}/man3/CosEventDomainAdmin_EventDomainFactory.*
%{_mandir}/man3/cosEventDomainApp.*
%endif

%files -n erlang-cosFileTransfer
%license COPYRIGHT
%license LICENSE.txt
%dir %{_libdir}/erlang/lib/cosFileTransfer-*/
%{_libdir}/erlang/lib/cosFileTransfer-*/ebin
%{_libdir}/erlang/lib/cosFileTransfer-*/include
%{_libdir}/erlang/lib/cosFileTransfer-*/src
%if %{with doc}
%{_mandir}/man3/cosFileTransferApp.*
%{_mandir}/man3/CosFileTransfer_Directory.*
%{_mandir}/man3/CosFileTransfer_File.*
%{_mandir}/man3/CosFileTransfer_FileIterator.*
%{_mandir}/man3/CosFileTransfer_FileTransferSession.*
%{_mandir}/man3/CosFileTransfer_VirtualFileSystem.*
%endif

%files -n erlang-cosNotification
%license COPYRIGHT
%license LICENSE.txt
%dir %{_libdir}/erlang/lib/cosNotification-*/
%{_libdir}/erlang/lib/cosNotification-*/ebin
%{_libdir}/erlang/lib/cosNotification-*/include
%{_libdir}/erlang/lib/cosNotification-*/src
%if %{with doc}
%{_mandir}/man3/CosNotification.*
%{_mandir}/man3/CosNotification_AdminPropertiesAdmin.*
%{_mandir}/man3/cosNotificationApp.*
%{_mandir}/man3/CosNotification_QoSAdmin.*
%{_mandir}/man3/CosNotifyChannelAdmin_ConsumerAdmin.*
%{_mandir}/man3/CosNotifyChannelAdmin_EventChannel.*
%{_mandir}/man3/CosNotifyChannelAdmin_EventChannelFactory.*
%{_mandir}/man3/CosNotifyChannelAdmin_ProxyConsumer.*
%{_mandir}/man3/CosNotifyChannelAdmin_ProxyPullConsumer.*
%{_mandir}/man3/CosNotifyChannelAdmin_ProxyPullSupplier.*
%{_mandir}/man3/CosNotifyChannelAdmin_ProxyPushConsumer.*
%{_mandir}/man3/CosNotifyChannelAdmin_ProxyPushSupplier.*
%{_mandir}/man3/CosNotifyChannelAdmin_ProxySupplier.*
%{_mandir}/man3/CosNotifyChannelAdmin_SequenceProxyPullConsumer.*
%{_mandir}/man3/CosNotifyChannelAdmin_SequenceProxyPullSupplier.*
%{_mandir}/man3/CosNotifyChannelAdmin_SequenceProxyPushConsumer.*
%{_mandir}/man3/CosNotifyChannelAdmin_SequenceProxyPushSupplier.*
%{_mandir}/man3/CosNotifyChannelAdmin_StructuredProxyPullConsumer.*
%{_mandir}/man3/CosNotifyChannelAdmin_StructuredProxyPullSupplier.*
%{_mandir}/man3/CosNotifyChannelAdmin_StructuredProxyPushConsumer.*
%{_mandir}/man3/CosNotifyChannelAdmin_StructuredProxyPushSupplier.*
%{_mandir}/man3/CosNotifyChannelAdmin_SupplierAdmin.*
%{_mandir}/man3/CosNotifyComm_NotifyPublish.*
%{_mandir}/man3/CosNotifyComm_NotifySubscribe.*
%{_mandir}/man3/CosNotifyFilter_Filter.*
%{_mandir}/man3/CosNotifyFilter_FilterAdmin.*
%{_mandir}/man3/CosNotifyFilter_FilterFactory.*
%{_mandir}/man3/CosNotifyFilter_MappingFilter.*
%endif

%files -n erlang-cosProperty
%license COPYRIGHT
%license LICENSE.txt
%dir %{_libdir}/erlang/lib/cosProperty-*/
%{_libdir}/erlang/lib/cosProperty-*/ebin
%{_libdir}/erlang/lib/cosProperty-*/include
%{_libdir}/erlang/lib/cosProperty-*/src
%if %{with doc}
%{_mandir}/man3/cosProperty.*
%{_mandir}/man3/CosPropertyService_PropertiesIterator.*
%{_mandir}/man3/CosPropertyService_PropertyNamesIterator.*
%{_mandir}/man3/CosPropertyService_PropertySet.*
%{_mandir}/man3/CosPropertyService_PropertySetDef.*
%{_mandir}/man3/CosPropertyService_PropertySetDefFactory.*
%{_mandir}/man3/CosPropertyService_PropertySetFactory.*
%endif

%files -n erlang-cosTime
%license COPYRIGHT
%license LICENSE.txt
%dir %{_libdir}/erlang/lib/cosTime-*/
%{_libdir}/erlang/lib/cosTime-*/ebin
%{_libdir}/erlang/lib/cosTime-*/include
%{_libdir}/erlang/lib/cosTime-*/src
%if %{with doc}
%{_mandir}/man3/cosTime.*
%{_mandir}/man3/CosTimerEvent_TimerEventHandler.*
%{_mandir}/man3/CosTimerEvent_TimerEventService.*
%{_mandir}/man3/CosTime_TimeService.*
%{_mandir}/man3/CosTime_TIO.*
%{_mandir}/man3/CosTime_UTO.*
%endif

%files -n erlang-cosTransactions
%license COPYRIGHT
%license LICENSE.txt
%dir %{_libdir}/erlang/lib/cosTransactions-*/
%{_libdir}/erlang/lib/cosTransactions-*/ebin
%{_libdir}/erlang/lib/cosTransactions-*/include
%{_libdir}/erlang/lib/cosTransactions-*/src
%if %{with doc}
%{_mandir}/man3/cosTransactions.*
%{_mandir}/man3/CosTransactions_Control.*
%{_mandir}/man3/CosTransactions_Coordinator.*
%{_mandir}/man3/CosTransactions_RecoveryCoordinator.*
%{_mandir}/man3/CosTransactions_Resource.*
%{_mandir}/man3/CosTransactions_SubtransactionAwareResource.*
%{_mandir}/man3/CosTransactions_Terminator.*
%{_mandir}/man3/CosTransactions_TransactionFactory.*
%endif

%files -n erlang-ic
%license COPYRIGHT
%license LICENSE.txt
%dir %{_libdir}/erlang/lib/ic-*/
%{_javadir}/erlang/ic.jar
%{_libdir}/erlang/lib/ic-*/ebin
%{_libdir}/erlang/lib/ic-*/include
%{_libdir}/erlang/lib/ic-*/priv
%{_libdir}/erlang/lib/ic-*/src
%{_libdir}/erlang/usr/include/erlang.idl
%{_libdir}/erlang/usr/include/ic.h
%{_libdir}/erlang/usr/lib/libic.a
%if %{with doc}
%{_mandir}/man3/ic.*
%{_mandir}/man3/ic_clib.*
%{_mandir}/man3/ic_c_protocol.*
%endif

%files -n erlang-orber
%license COPYRIGHT
%license LICENSE.txt
%dir %{_libdir}/erlang/lib/orber-*/
%{_libdir}/erlang/lib/orber-*/COSS
%{_libdir}/erlang/lib/orber-*/ebin
%{_libdir}/erlang/lib/orber-*/include
%{_libdir}/erlang/lib/orber-*/priv
%{_libdir}/erlang/lib/orber-*/src
%if %{with doc}
%{_mandir}/man3/CosNaming.*
%{_mandir}/man3/CosNaming_BindingIterator.*
%{_mandir}/man3/CosNaming_NamingContext.*
%{_mandir}/man3/CosNaming_NamingContextExt.*
%{_mandir}/man3/Module_Interface.*
%{_mandir}/man3/any.*
%{_mandir}/man3/corba.*
%{_mandir}/man3/corba_object.*
%{_mandir}/man3/fixed.*
%{_mandir}/man3/interceptors.*
%{_mandir}/man3/lname.*
%{_mandir}/man3/lname_component.*
%{_mandir}/man3/orber.*
%{_mandir}/man3/orber_acl.*
%{_mandir}/man3/orber_diagnostics.*
%{_mandir}/man3/orber_ifr.*
%{_mandir}/man3/orber_tc.*
%endif


%changelog
%autochangelog
