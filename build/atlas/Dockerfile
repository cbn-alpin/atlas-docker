ARG ATLAS_IMAGE

FROM ${ATLAS_IMAGE}

ARG UID
ARG GID
ARG HOST_USER

USER root
# Add the group (if not existing) then add the user to the group
RUN id --name --group ${GID} || \
    addgroup --gid ${GID} ${HOST_USER} && \
    id --name --user ${UID} || \
    adduser --gecos GECOS --disabled-password --uid ${UID} --gid ${GID} ${HOST_USER}