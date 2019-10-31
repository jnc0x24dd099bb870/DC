#!/usr/bin/python3

import updating_system
import installing_services
import source_update
import install_k8s

updating_system.Updates().upd()
updating_system.Updates().install()

installing_services.Services().docker_installing()
source_update.install()

install_k8s.Install().pip_client()
#install_k8s.Install().ins()

#still in progress, though... need to set-up others, like network
